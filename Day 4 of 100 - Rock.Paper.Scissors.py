import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))
options = [rock, paper, scissors]

print(options[player_choice])
if player_choice == 0:
  print("You picked ROCK")
elif player_choice == 1:
  print("You picked PAPER")
elif player_choice == 2:
  print("You picked SCISSORS")

computer = random.randint(0, 2)

print(options[computer])
if computer == 0:
  print("Computer picked ROCK")
elif computer == 1:
  print("Computer picked PAPER")
elif computer == 2:
  print("Computer picked SCISSORS")

if player_choice == computer:
    print("Its a draw")
elif player_choice == 0:
    if computer == 1:
        print("The Computer WINS")
    elif computer == 2:
        print("Player WINS")
elif player_choice == 1:
    if computer == 0:
        print("Player WINS")
    elif computer == 2:
        print("The Computer WINS")
elif player_choice == 2:
    if computer == 0:
        print("The Computer WINS")
    elif computer == 1:
        print("Player WINS")

input("Press enter to close")