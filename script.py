import random

rand_num = random.randint(0,10)
try_guess = 0
max_attempts = 3

while try_guess < max_attempts:
    try:
        input_num = int(input("Pick a number between 0 and 10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    try_guess += 1

    if rand_num == input_num:
        print("Well done!")
        break
    elif input_num < rand_num:
        print("Guess a bigger number.")
    else:
        print("Guess a lower number.")
        
    if try_guess == max_attempts:
        print(f"Game over. The number was {rand_num}.")