#this part imports the random choices to generate the list for the game
import random
from random import choice

#this part asks the player to start if they are ready by pressing Y
def game_start():
    start = "start"
    while start == "start":
        start = input("Enter Y to start the game when you are ready: ").upper()
        if start == "Y":
            print()
            True
        else:
            print("ohh!! leaving so quick D:, hope to see you soon ")
            quit()


#this part prints a welcome message and shows the player the instructions for the game
print("----------------------------------------")
print("            MASTERMIND GAME             ")
print("----------------------------------------")
print("--------How does the game work??--------")
print("1. The computer will generate 4 random fruits and you have to keep guessing until you get all of them right.")
print("2. the respective fruits are apple, orange, banana and kiwi")
print("3. keep in mind you may have more than one fruits in each list")
print("------GOOD LUCK AND HAPPY GUESSING------")
print("----------------------------------------")


game_start()

#the fruit list for the game
fruit_list=["APPLE", "ORANGE", "BANANA", "KIWI"]
 
play = "Y"
while play == "Y":
    #this loop generates the random list for the game and would generate a new one for every new game
    game_list= []
    for i in range (4):
        game_list.append(random.choice(fruit_list))
        
    
    #this loop start  counting the number of tries to display at the end and would display the number of the try at the start of each new one
    #the player is also given 15 tries else they must restart the game
    tries = 1
    while tries < 15:
        print("----------------------------------------")
        print ("this is try number " + str(tries))
        #this is to store the guesses inputted by the player
        player_guess= []

        #this loop is to input the guesses
        while True:
            first_fruit= input("Enter your first fruit: ").upper()
            #this appends the first guess into the guess list mentioned above 
            if first_fruit in fruit_list:
                player_guess.append(first_fruit)
                
                break
            else:
                #this part is to make sure that the input entered by the player is chosen from the list and will return the player to enter the guess again
                print("wrong input!!!, PLEASE enter fruits from the given list only, the fruits given are: ")
                print(" APPLE, BANANA, ORANGE, KIWI ")

        while True:
            print("----------------------------------------")
            second_fruit= input("Enter your second fruit: ").upper()

            if second_fruit in fruit_list:
                player_guess.append(second_fruit)

                break
            else:
                print("wrong input!!!, PLEASE enter fruits from the given list only, the fruits given are: ")
                print(" APPLE, BANANA, ORANGE, KIWI ")

        while True:
            print("----------------------------------------")
            third_fruit= input("Enter your third fruit: ").upper()

            if third_fruit in fruit_list:
                player_guess.append(third_fruit)

                break
            else:
                print("wrong input!!!, PLEASE enter fruits from the given list only, the fruits given are: ")
                print(" APPLE, BANANA, ORANGE, KIWI ")


        while True:
            print("----------------------------------------")
            fourth_fruit= input("Enter your fourth and last fruit: ").upper()

            if fourth_fruit in fruit_list:
                player_guess.append(fourth_fruit)

                break
            else:
                print("wrong input!!!, PLEASE enter fruits from the given list only, the fruits given are: ")
                print(" APPLE, BANANA, ORANGE, KIWI ")
        
        #these variables are to store the number of correct guess in correct place and the ones that are not in the crrect place
        correct_placement = 0
        correct_guess_only = 0
        #this for loop compares the guesses with the generated list to check if the guesses are correct AND in the correct place
        for i in range (4):
            if player_guess[i] == game_list[i]:
                correct_placement += 1
        #this for loop compares the guesses with the list again but to check if the guesses are correct and if they are not in the correct placement
        for i in range (4):
            if player_guess[i] in game_list and player_guess[i] != game_list[i]:
                correct_guess_only += 1

        #this if statement will check if the player got all of them correct and will congratulate and ask if they want to play again
        if correct_placement == 4:
            print(" CONGRATULATIONS!!!, YOU GUESSED CORRECTLY, YOU TOOK " + str(tries) + " TRIES")
            print(" the random generated list was " + str(game_list) )

            break
        #else if not all the guesses were correct it will show him how many were correct and how many were correct but not in the correct place and will also show the number tries taken
        else:
            print(" the number of correct guess in place is " + str(correct_placement))
            print(" the number of correct guess but in the wrong place is " + str(correct_guess_only))
            tries += 1
        #this if statement is to check whether the player has exceeded the allowed number of attempts, if so it will show him the generated list and will stop the game
        if tries == 15:
            print(" sorry you could not make the correct guesses but the game is over!!")
            print(" This was the list generated by the computer " + str(game_list))
    #this whole part is to ask the player if they want to play again after they finished their attempts whether they won or exceeded number of attempts
    print()
    play = input("Would you like to play again, enter 'Y' to play or 'N' to quit: ").upper()
    #this first part of the if statement will check if the player doesnt want to play anymore and will stop the program if so
    if play == "N" or play == "n":
        print("Thank you for playing i hope you enjoyed, see you next time.....")
    else:
        #this loop is to ensure the player enters the correct command
        while play != "Y" or play != "N":
            print("WRONG INPUT, enter 'Y' to play again or 'N' to quit")
            play = input("Would you like to play again, enter 'Y' to play or 'N' to quit: ").upper()
            break

    

            


        
                  
            

                                                                            
                
                
                    
        
        





















                
        

        
                        





