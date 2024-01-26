import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

computer_choice = random.randint(0, 2)

print("Computer choice: ")

print(computer_choice)
if user_choice == computer_choice: 
    result = "It's a tie!"
elif(user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    result = "You win!"
else:
    result = "Computer Wins!"

print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")
print(result)