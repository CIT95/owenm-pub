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

rps = [rock, paper, scissors]

playerchoice = int(input("Make your choice! Type 1 for rock, 2 for paper, and"
                         " 3 for scissors.\n"))-1

# Cheating code below:
cheat = random.randint(0, 9)
if cheat >= 0 and cheat <= 3:
    computerchoice = random.randint(0, 2)
else:
    if playerchoice == 2:
        computerchoice = 0
    else:
        computerchoice = playerchoice + 1


if playerchoice > 2 or playerchoice < 0:
    print("That's an invalid choice! You lose!")
else:
    # lines 38-40 are my solution to Dr. Angela's debug challenge.
    print(rps[playerchoice])
    print("Computer chose:")
    print(rps[computerchoice])
    if playerchoice == computerchoice:
        print(f"It's a tie!")
    elif (playerchoice == 0 and computerchoice == 1) or \
         (playerchoice == 1 and computerchoice == 2) or \
         (playerchoice == 2 and computerchoice == 0):
        print(f"You lose.")
    elif (playerchoice == 0 and computerchoice == 2) or \
         (playerchoice == 1 and computerchoice == 0) or \
         (playerchoice == 2 and computerchoice == 1):
        print(f"You win!")
