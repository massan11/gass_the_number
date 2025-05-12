import random
rand_num = random.randint(0,10)

try_guess = 0
while try_guess < 3:
    input_num = int(input("Pick a number between 0 and 10: "))
    if rand_num == input_num:
        print("Well done!")
        break
    elif input_num < rand_num:
        try_guess += 1
        if try_guess < 3:
            print("Guess a bigger number.")
        else:
            print("Game over.")
        
    elif input_num > rand_num:
        try_guess += 1
        if try_guess < 3:
            print("Guess a lower number.")
        else:
            print("Game over.")
    else:
        print("Erorr!")