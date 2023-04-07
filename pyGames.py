
import random 

#defines the function 
def rps(): 
    
        try:
            print("Let's play rock paper scissors!")
            #makes user make a choice
            game = input("Please make your choice and enter 'rock', 'paper', or 'scissors'. ")
            user_choice= ["rock", "paper", "scissors"]
            #sets program to make a random choice from the choices the user can make 
            rand_choice= random.choice(user_choice)

            print("The computer played " + rand_choice )

            #sets up conditions 
            if game == rand_choice: 
                print("It's a tie")

            elif game ==  "rock":
                if rand_choice== "scissors":
                    print("You win!!")
                    #win will be saved as True and used in main function
                    return True
                  
                else:
                    print("You lose. Sorry!")
                    return False

            elif game == "paper":
                if rand_choice == "rock":
                    print("You win!!")
                    return True
                else:
                    print("You lose. Sorry!")
                    return False

            elif game == "scissors":
                if rand_choice == "paper":
                    print("You win!!")
                    return True
                else:
                    print("You lose. Sorry!")
                    return False
            else:
                raise ValueError
        except ValueError:
            print("Please try again, your input cannot be read. You must only enter the word 'rock', 'paper', or 'scissors'")
        


def headsOrTails():
        try:
        
            print("Welcome to the the coin flip simulator!")
            choice = int(input("Please guess whether a coin flip will be heads or tails. To guess heads, please enter '1'. To guess tails, please enter '2'."))
            flip = random.randint(1,2)
            if flip == 1:
                print("The coin landed on heads.")
            elif flip == 2:
                print("The coin landed on Tails.") 
            if choice == flip:  
                print("You guessed correctly!")
                return True 
              

            elif choice != flip: 
                print("Sorry, you did not guess correctly.")
                return False 
            else:
                #if anything besides theh expected is entered, a error will be raised
                raise ValueError
        except ValueError:
            #if an error is raised, the print statment will run
            print("You must enter either the number '1' or '2' as your choice.")
        

def chamChamCham(): 
        try: 
            
            print(" Hello! So I hear you want to play a game of Cham Cham Cham, but lets go over the rules first. \n To play, decide if you want to look left, right, up or down. \n The computer will choose where it wants to point and if it's in the same direction you look, YOU LOSE! \n Chose wisely friend! ")
            game = input("Please choose between looking 'left', 'right', 'up' or 'down'. \n Be sure to type your answer as shown! \n ")
            user_choice= ["left", "right", "up", "down"]
            rand_choice= random.choice(user_choice)

            #prints the random choice by the computer 
            print("The computer pointed " + rand_choice )

            if game == rand_choice: 
                print("You Lose! Sorry friend.")
                return False

            #!= stands for does not equal 
            elif game !=  rand_choice:
                print("You win!!")
                return True 
            else:
               raise ValueError

        except ValueError:
            print("Please only enter 'left', 'right', 'up' or 'down' as your choice!")

def main():
    
    #defines the variables to be used
    win = 0
    lose = 0
    
    while 1:
        try:
            print("Welcome back to the game simulator!")
            print("You can play rock paper scissors, cham cham cham, or flip a coin. ")
            #has the user choose a game to play
            gameChoice = input("Please enter 'R' for rock paper scissors, 'F' for a coin flip, or 'C' for cham cham cham. If you would like to quit, please type 'Q'. ")

            #depending on what the user plays, the result will differ 
            if gameChoice == 'R': 
                result = rps()
                #if the result is true, which is defined in above fucntions, the variable win will have 1 added to it 
                if result == True:
                    win = win + 1
                elif result ==  False:
                    lose = lose + 1
            
                    
            elif gameChoice == 'F': 
                result =  headsOrTails()
                if result == True:
                    win = win + 1
                elif result ==  False:
                    lose = lose + 1

                
            elif gameChoice == 'C':
                result = chamChamCham()
                if result == True:
                    win = win + 1
                elif result ==  False:
                    lose = lose + 1

            elif gameChoice == 'Q':
                print("Thank you for playing!! The number of wins and losses are reported below. ")
                #will print the total wins/losses
                print("There were " + str(win) + " wins and " + str(lose) + " losses ")
                break

            else:
                raise ValueError
        except ValueError:
            print("Invalid imput. Please follow te promts.")


        

if __name__ == '__main__':
    main()
