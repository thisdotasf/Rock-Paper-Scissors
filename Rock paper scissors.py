import random

def invalid(reason):
    return "Quited program due to: " + reason

options = ["Rock", "Paper", "Scissors"]

data = "Choose an option. (1 = rock, 2 = paper, 3 = scissors)"
player_choice = input(data)

pChoice = ""
dPlayer = 0

if player_choice.isdigit():
    player_choice = int(int(player_choice) - 1) # Becuase array starts on 0
    if 2 >= player_choice >= 0:
        pChoice = options[player_choice]
        dPlayer = player_choice
    else:
        pChoice = options[0]
        print("Automaticlly choose rock due to invalid number.")
else:
    print(invalid("Not a digit."))
    quit()

print("Your choice is: " + pChoice)

ai_choice = random.randint(0,2)
d_aiChoice = int(ai_choice)
ai_choice = options[ai_choice]

print("Computer choice is: " + ai_choice)

def tie(): print("Its a tie.")
def win(): print("You win.")
def lose(): print("You lose.")


if dPlayer == 0 and d_aiChoice == 0: tie()
elif dPlayer == 1 and d_aiChoice == 1: tie()
elif dPlayer == 2 and d_aiChoice == 2: tie()
elif dPlayer == 0 and d_aiChoice == 2: win()
elif dPlayer == 2 and d_aiChoice == 1: win()
elif dPlayer == 1 and d_aiChoice == 0: win()
elif dPlayer == 2 and d_aiChoice == 0: lose()
elif dPlayer == 1 and d_aiChoice == 2: lose()
elif dPlayer == 0 and d_aiChoice == 1: lose()