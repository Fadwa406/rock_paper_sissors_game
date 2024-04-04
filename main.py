import random

paper_ascii = ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___) 
    
  """)
rock_ascii = ("""
  _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)

  """)
sissors_ascii = ("""
  _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)

print("Welcome to the Rock, Paper, Sissors game!")
choice = input("Please type in help if you need the instructions or you can press enter to start the game ").lower()
if choice == "help".lower():
  print(
    """
    **** Help ****
    Rock beats Sissors
    Paper beats Rock
    Sissors beats Paper
    """
  )
  
#the user is choosing
user_choice = input("Please choose Rock or Paper or Sissors: ").lower()

# print the user's choice
if user_choice == "rock":
  print(f"You chose: \n{rock_ascii}")
elif user_choice == "paper":
  print(f" You chose \n{paper_ascii}")
else:
  print(f"You chose \n{sissors_ascii}")
  
# the computer is choosing randomly 
computer_chocie = random.choice(['rock', 'paper', 'sissors'])

#printing out the cp's choice
if computer_chocie == "rock":
  print(f"Computer chose \n{rock_ascii}")
elif computer_chocie == "paper":
  print(f"Computer chose \n{paper_ascii}")
else:
  print(f"Computer chose \n{sissors_ascii}")


if user_choice == computer_chocie:
  print("It's a tie!")
elif(
  (user_choice == "rock" and computer_chocie == "sissors")
  or(user_choice == "paper" and computer_chocie == "rock")
  or(user_choice == "sissors" and computer_chocie == "paper")
):
  print(f"You won! {user_choice} beats {computer_chocie}")
else:
  print(f"You lost {computer_chocie} beats {user_choice}")
  
