# Make a two-player Rock-Paper-Scissors game. One of the players is the computer.
# 10 rounds. Print out the winner and points earned by both players at the end of the game.
# Remember the rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# - You will need to import 'random' and use random.choice() to
# make the computer choice in each round random.
# - Use a Dictionary to store the choices made by the Player and
# the Computer in each round along with the winner of that round.
# You should be able to print out the details of each round once the game is completed.
# Example -
# Enter the round for which you need the information >> 3
# Output
# Player choice = Rock
# Computer choice = Paper
# Player won Round 3
from random import randint
# Step 1: Loop 10 times with input 0, 1, or 2 (rock, paper, scissors)
Dict_user = {}
Dict_computer = {}
Dict_result = {}
early_return = False
for i in range(0, 9):
    choice = int(input("Please enter a choice(0 for rock, 1 for paper, or 2 for scissors): "))
    if(choice != 0 and choice != 1 and choice != 2):
        print("Error: Input is not in the range (0-2)..Break")
        early_return = True
        break
    Dict_user[i] = choice
    # Step 2: Generate random number between 0 and 2(inclusive) to represent input from the computer
    choice_comp = randint(0, 2)
    Dict_computer[i] = choice_comp
    #Step 3: Compare choices
    if(choice == 0): #rock
        if(choice_comp == 0): #rock
            Dict_result[i] = "Tie"
        elif(choice_comp == 1): #paper
            Dict_result[i] = "Computer won"
        else: #scissors
            Dict_result[i] = "User won"
    elif(choice == 1): #paper
        if (choice_comp == 0): #rock
            Dict_result[i] = "User won"
        elif (choice_comp == 1): #paper
            Dict_result[i] = "Tie"
        else: #scissors
            Dict_result[i] = "Computer won"
    else: #scissors
        if (choice_comp == 0): #rock
            Dict_result[i] = "Computer won"
        elif (choice_comp == 1):  # paper
            Dict_result[i] = "User won"
        else:  # scissors
            Dict_result[i] = "Tie"

index = int(input("Which run(1-10) would you like to access? "))
if(index < 1 or index > 10):
    print("Error: Input is not in the range (1-10)..Exiting")
else:
    if(early_return == False):
        print(Dict_user[index - 1])
        print(Dict_computer[index - 1])
        print(Dict_result[index - 1])
    else:
        print("No results to display.")