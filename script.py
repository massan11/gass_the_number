import random

while True:

    difficulty = input("Choose the game difficulty (easy/medium/hard): ").strip().lower()

    if difficulty == "easy":
        max_num = 5
    elif difficulty == "medium":
        max_num = 10
    elif difficulty == "hard":
        max_num = 20
    else:
        print("Invalid difficulty. Defaulting to medium.")
        max_num = 10

    rand_num = random.randint(0, max_num)
    try_guess = 0
    max_attempts = 3

    while try_guess < max_attempts:
        try:
            input_num = int(input(f"You have {max_attempts - try_guess} chances. Pick a number between 0 and {max_num}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        try_guess += 1

        if rand_num == input_num:
            print(f"Well done! You guessed it in {try_guess} {'try' if try_guess == 1 else 'tries'}!")
            break
        elif input_num < rand_num:
            if try_guess != max_attempts:
                print("Guess a bigger number.")
        else:
            if try_guess != max_attempts:
                print("Guess a lower number.")
            
        if try_guess == max_attempts:
            print(f"Game over. The number was {rand_num}.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break
