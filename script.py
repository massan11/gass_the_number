import random
rand_num = random.randint(0,10)

input_num = int(input("Pick a number between 0 and 10: "))

if rand_num == input_num:
    print("Well done!")
else:
    print(f"You made a mistake, the number was {rand_num}. ")