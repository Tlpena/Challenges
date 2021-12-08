import random
import colorama



def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(": this is not a number, try again")


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print('\u001b[36m', "Please guess higher")
        else:
            print('\u001b[35m', "Please guess lower")
