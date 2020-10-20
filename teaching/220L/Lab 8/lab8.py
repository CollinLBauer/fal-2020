# Name:
# lab8.py

def format_practice():
    print("This function displays several formatted strings.")

    # print("The value of {} is {}.".format(_____))
    # Expected: The value of x is 19.

    # print("It's raining {1} and {0}".format(_____))
    # Expected: It's raining cats and dogs

    # print("My name is {0}, {1} {0}".format(_____))
    # Expected: My name is Bond, James Bond

    # print(_____.format(2.3, 0.4567))
    # Expected: 2.30 0.457

    # print(_____.format(3, 7.4589))
    # Expected: Time left: 03:07.46

    # print(_____.format("Steph", "Curry", 43.75432))
    # Expected: Steph Curry: 43.75


def binary_list(n):
    from math import log2
    numbers = []
    for i in range(n):
        # bin() converts a number to binary, but without leading 0's
        # str.zfill() left-pads a string with zeros
        number = bin(i)[2:].zfill(int(log2(n)))
        numbers.append(number)
    return numbers
