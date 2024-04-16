from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
        player = input("Rock, Paper, Scissors?")

        while player != "Rock" and player != "Paper" and player != "Scissors":
                player = input("Rock, Paper, Scissors?")
                
        print("Computer picks",computer)
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
                        
        player == False
        computer = t[randint(0,2)]