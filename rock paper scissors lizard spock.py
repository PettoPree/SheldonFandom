from random import randint

# create a list of play options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# assign a random play to the computer
computer = t[randint(0, 4)]

# set player to False
player = False

while not player:
    # set player to True
    player = input("Rock, Paper, Scissors, Lizard, Spock?\n")

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
        else:
            print("You win!", player, "vaporizes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        elif computer == "Lizard":
            print("You win!", player, "eats", computer)
        else:
            print("You win!", player, "disproves", computer)
    elif player == "Scissors":
        if computer == "Lizard":
            print("You win!", player, "decapitates", computer)
        else:
            print("You lose!", computer,"smashes",player)
    elif player == 'Lizard':
        if(computer=='Spock'):
                print('you lose!',computer,'poisons',player)    
    else:
        print("That's not a valid play. Check your spelling!")

    # set both back to False so the loop continues
    player = False
    computer = t[randint(0, 4)]
