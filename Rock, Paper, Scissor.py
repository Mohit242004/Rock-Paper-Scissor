"""
WORKFLOW OF PROJECT :
1 - Input from user(Rock, Paperm scissror)
2 - Computer choice (Computer will choose randomly not conditionally)
3 - Result print

Cases :
A - Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - Paper 
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor 
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""


import random
list_items = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(list_items)

print(f"User Choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Choices are Same = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer win")
    else :
        print("Rock Smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper = Computer win")
    else :
        print("Paper Covers Rock = You win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock Smashes Scissor = Computer win")
    else:
        print("Scissor Cuts Paper = You win")