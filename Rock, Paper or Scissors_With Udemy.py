# -*Data structure*-
"""
Created on Mon Aug 26 10:14:12 2024

@author: Shokhrukh
"""
import random
# friends=['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
# print(random.choice(friends))

# choice=random.randint(0, 4)
# print(friends)

# states_of_america = [
#     "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]
#print(len(states_of_america))

# EWG's Dirty Dozen List for 2023

# # Group 1: Fruits
# fruits = [
#     "Strawberries",
#     "Nectarines",
#     "Apples",
#     "Grapes",
#     "Cherries",
#     "Peaches",
#     "Pears",
#     "Tomatoes"  # Technically a fruit
# ]

# # Group 2: Vegetables
# vegetables = [
#     "Spinach",
#     "Kale, Collard & Mustard Greens",
#     "Bell and Hot Peppers",
#     "Celery"
# ]

# dirty_dozen=[fruits, vegetables]
# print(dirty_dozen)

# print(states_of_america[-1])

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
r_p_s_names=['Rock', 'Paper', 'Scissors']
r_p_s=[Rock, Paper, Scissors]

choice_user=int(input("What do u choose? Type 0 for Rock. 1 for Paper or 2 for Scissors\n"))
print(f"You chose : {r_p_s_names[choice_user]}")
print(r_p_s[choice_user])

choice_pc=random.randint(0,2)
print(f"Computer chose: {r_p_s_names[choice_pc]}")
print(r_p_s[choice_pc])

if choice_user>=3 or choice_user<0:
    print("You typed an invalid number. You lose!")
elif choice_pc==2 and choice_user==0:
    print("You win!")
elif choice_pc==0 and choice_user==2:
    print("You lose!")
elif choice_pc>choice_user:
    print("You lose!")
elif choice_pc<choice_user:
    print("You win!")
elif choice_pc==choice_user:
    print("It's a draw!")































