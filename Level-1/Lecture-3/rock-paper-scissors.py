import random 
# defaining constants 
ROCK = 1
PAPER = 2
SCISSORS = 3    
# print(random.randint(1,5)) # sample 
print("Rock, Paper and Scissors: ")
computer_number = random.randint(1,3)
print("""Options: 
1. Rock 
2. Paper 
3. Scissors""") 
user_number = int(input("Enter you're choice(1-3): "))
computer_choice = "ROCK"
user_choice = "ROCK"
# finding out computer choice 
if computer_number == ROCK: 
    computer_choice = "ROCK"
elif computer_number == PAPER:
    computer_choice = "PAPER"
elif computer_number == SCISSORS: 
    computer_choice = "SCISSORS"
# finding out user choice 
if user_number == ROCK: 
    user_choice = "ROCK"
elif user_number == PAPER: 
    user_choice = "PAPER" 
elif user_number == SCISSORS: 
    user_choice = "SCISSORS"

print(f"Computer Choice: {computer_choice}")
print(f"User Choice: {user_choice}")