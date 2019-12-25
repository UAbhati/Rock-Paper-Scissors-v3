import random
import time
newlist = ["ROCK","PAPER","SCISSORS"]
print("ROCK.....")
print("PAPER.....")
print("SCISSORS.....")
print("# INSTRUCTION :: This Game will till Someone Score 3. However Score 3 first will be Winner")
print("\t\t You can type full name of your choice like rock, paper, scissors \n\t\t   or Just type first letter of your choice like r for Rock")
print("\t\t You can type quit or q to stop the game")
print("\nLet's Start the Game")
Pwin = 0
Cwin = 0
print("Ready for the first Try")
while Pwin < 3 and Cwin < 3:
    print("\n")
    player = input("###  It's Player move : ").upper()
    if(player == "QUIT" or player == "Q"):
        break
    rand_num = random.randint(0,2)
    computer = newlist[rand_num]
    print(f"###  Computer choose : {computer}\n")
    if player == computer:
        print("It's a Tie!")
    elif (player == "ROCK" or player == "R") and computer == "PAPER":
        print("Computer WINS!")
        Cwin += 1
    elif (player == "ROCK" or player == "R") and computer == "SCISSORS":
        print("Player WINS!")
        Pwin += 1
    elif (player == "SCISSORS" or player == "S") and computer == "PAPER":
        print("Player WINS!")
        Pwin += 1
    elif (player == "SCISSORS" or player == "S") and computer == "ROCK":
        print("Computer WINS!")
        Cwin += 1
    elif (player == "PAPER" or player == "P") and computer == "ROCK":
        print("Player WINS!")
        Pwin += 1
    elif (player == "PAPER" or player == "P") and computer == "SCISSORS":
        print("Computer WINS!")
        Cwin += 1
    else :
        print("You have not enter a valid choice, Try Again!")
    time.sleep(1)
    print("\n\t######## Scores till Now ########")
    print(f"\t### Player Score is : {Pwin} ###")
    print(f"\t### Computer Score is : {Cwin} ###\n")
    print("\nReady for Next Try")
print("\nCalculating the Final Scores......\n")
time.sleep(2)
print("\n********Final Standings********")
if Pwin > Cwin:
    print("***** CONGRATS :), You WINS! *****\n")
    print(f"Player Score is : {Pwin}")
    print(f"Computer Score is : {Cwin}")
elif Pwin < Cwin:
    print("***** SORRY :(, Computer WINS! *****\n")
    print(f"Player Score is : {Pwin}")
    print(f"Computer Score is : {Cwin}")
elif Pwin == Cwin:
    print("***** It's a Tie! *****\n")
    print(f"Player Score is : {Pwin}")
    print(f"Computer Score is : {Cwin}")
else :
    print("Something want Wrong")
