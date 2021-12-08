def division():

    chosen_number1 = int(input("Please chose a number: "))
    chosen_number2 = int(input("Please chose another number: "))
    divided_answer = chosen_number1/chosen_number2

    print("{} divided by {} is equal to {}".format(chosen_number1, chosen_number2, divided_answer))


def getint():
    while True:
        try:
            number = int(input("Pleas enter a number"))
            return number
        except ValueError:
            print("Invalid number selected, please try again")


try:
    print(division())
except (ZeroDivisionError, ValueError):
    print("way to go, you broke it")

