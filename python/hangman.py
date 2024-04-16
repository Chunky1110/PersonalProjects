# This is a simple program to play hangman I used to teach myself the python basics
# Carson Crockett

# Function to print different stages of hanging
# Takes a life parameter that indicates how many wrong answers the player has made and prints the appropriate stage
def hang(life):
        if life == 0:
                print("-----------")
                print("|")
                print("|")
                print("|")
                print("|")
                print("----")
        elif life == 1:
                print("-----------")
                print("|       O")
                print("|")
                print("|")
                print("|")
                print("----")
        
        elif life == 2:
                print("-----------")
                print("|       O")
                print("|       |")
                print("|")
                print("|")
                print("----")
        
        elif life == 3:
                print("-----------")
                print("|       O")
                print("|      /|")
                print("|")
                print("|")
                print("----")
        
        elif life == 4:
                print("-----------")
                print("|       O")
                print("|      /|\\")
                print("|")
                print("|")
                print("----")

        elif life == 5:
                print("-----------")
                print("|       O")
                print("|      /|\\")
                print("|      /")
                print("|")
                print("----")
        
        elif life == 6:
                print("-----------")
                print("|       O")
                print("|      /|\\")
                print("|      / \\")
                print("|")
                print("----")

# Function to determine if a win has been achieved
def win(game_board):
        # Check if all empty spaces have been filled on the board
        if game_board.count("_") == 0:
                print("YOU WIN")
                return True
        else:
                return False

# Function to print current state of the board
def board(str, game_board):
        # Print each character in the board w/o a newline except for the last
        for index in range(0,len(str)):
                if(index != len(str) - 1):
                        print(game_board[index], end = " ")
                else:
                        print(game_board[index])
                        
# Function to update the board with a correct guess
def correct(letter, index, game_board):
        # Takes in the string of the complete phrase/word, the letter guessed by the player
        # The index of the letter in the phrase/word, and the board array
                
        # Remove empty space at index and replace with guessed letter
        if(game_board[index] == "_"):
                game_board.pop(index)
                game_board.insert(index, letter)
        else:
                print("Character already guessed, try again")
        
#Function which runs the game once
def game(end_game, guess_board): 
        #Number of incorrect guesses until the game is lost
        #Set to six because theyre are six phases of the hanging man
        lives = 6
        
        #Take in input for what the word/phrase will be
        #Can be a single word or sentence
        guess_word = input("What is the word?: ")
        
        #Create empty board
        for x in range(0,len(guess_word)):
                if guess_word[x] == " ":
                        guess_board.append(" ")
                else:
                        guess_board.append("_")
                
        #Print the first hanging frame (empty)
        hang(0)
        #Print an empty board
        board(guess_word,guess_board)
        
        #take guesses until game is not over
        while not end_game:
                #Take in player guess
                guess = input("what is your guess?: ")
                print()
                
                #initalize boolen to track if answer was correct or not
                answer = False
                
                #Check player guess
                #Non-Case Sensitive
                
                #if word is guessed player wins
                if guess.lower() == guess_word.lower():
                        print("You guessed it!")
                        answer = True
                        end_game = True
                        
                #ignore spaces
                elif guess == " ":
                        hang(6 - lives)
                        board(guess_word,guess_board)
                        print("Spaces are not a valid guess")
                        
                #check word for matching letters
                else:
                        #loop through word and check to see if guessed character is in the word
                        for i in range(0,len(guess_word)):
                                if guess == " ":
                                        hang(6 - lives)
                                        board(guess_word,guess_board)
                                        print("Spaces are not a valid guess")
                                        answer = True
                                        break
                                #change case when needed to match phrase
                                elif guess == guess_word[i]:
                                        if answer:
                                                correct(guess, i, guess_board)
                                        else:
                                                hang(6 - lives)
                                                correct(guess, i, guess_board)
                                        answer = True
                                elif guess == guess_word[i].upper():
                                        if answer:
                                                correct(guess.lower(), i, guess_board)
                                        else:
                                                hang(6 - lives)
                                                correct(guess.lower(), i, guess_board)
                                        answer = True
                                elif guess == guess_word[i].lower():
                                        if answer:
                                                correct(guess.upper(), i, guess_board)
                                        else:
                                                hang(6 - lives)
                                                correct(guess.upper(), i, guess_board)
                                        answer = True
                        #print their board
                        board(guess_word,guess_board)
        
                #if answer is incorrect subtract one life and print board and hangman
                if answer == False:
                        lives -= 1
                        hang(6 - lives)
                        board(guess_word,guess_board)
                        
                #if player runs out of lives or guessed the entire word end the game
                if lives == 0 or win(guess_board):
                        end_game = True
 
#declare the board
board_array = []
#boolean to determine when game is over
game_over = False

#empty the board and start the game
board_array.clear() 
game(game_over, board_array)

#ask if player wants to play again and verify input
play_again = input("Game Over! Play again? (Y/N) ")
while play_again != "Y" and play_again != "N"  and play_again != "y" and play_again != "n": 
        play_again = input("Game Over! Play again? (Y/N)")
        
#keep playing until player says to stop
while play_again == "Y" or play_again == "y":
        game_over = False
        board_array.clear()
        game(game_over,board_array)
        play_again = input("Game Over! Play again? (Y/N)")
        while play_again != "Y" and play_again != "N"  and play_again != "y" and play_again != "n": 
                play_again = input("Game Over! Play again? (Y/N)")