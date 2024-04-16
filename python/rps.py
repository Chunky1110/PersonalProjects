# Simple Rock Paper Scissors program I used to teach myself the basics of Python
# Carson Crockett

from random import randint

# Create a set containing the three options
t = ["Rock", "Paper", "Scissors"]

# Generate a random choice as the opponent
computer = t[randint(0,2)]

player = False

# Infinitely loop until break statement is called
while True:
        # Take the input from the player for the current round
        player = input("Rock, Paper, Scissors?")

        # Validate input
        while player != "Rock" and player != "Paper" and player != "Scissors":
                player = input("Rock, Paper, Scissors?")
                
        # Print computer choice
        print("Computer picks",computer)
        
        # Determine who wins the round and print appropriate response
        if player == computer:
                print("Tie!")
        elif player == "Rock":
                if computer == "Paper":
                        print("You Lose!", computer, "beats", player)
                if computer == "Scissors":
                        print("You win", player, "beats", computer)
        
        elif player == "Paper":
                if computer == "Scissors":
                        print("You Lose!", computer, "beats", player)
                if computer == "Rock":
                        print("You win", player, "beats", computer)
                        
        else:
                if computer == "Rock":
                        print("You Lose!", computer, "beats", player)
                if computer == "Paper":
                        print("You win", player, "beats", computer)
        
        # Determine if player wants to play more and break loop if no
        answer = input("Do you want to play again [Y/N]\n")
        if input == 'N' or input == 'n':
                break
        while input != 'Y' and input != 'y' and input != 'N' and input != 'n':
                print("Invalid input\n")
        
        computer = t[randint(0,2)]