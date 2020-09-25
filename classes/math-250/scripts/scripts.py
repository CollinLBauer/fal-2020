from sys import argv
from math import sqrt


def numbify(values):
    try:
        for i in range(len(values)):
            temp = values[i]
            values[i] = float(values[i])
    except:
        print("Value \"{}\" is not a number.".format(temp))
        exit()


def mean(values):    
    total = 0
    for val in values:
        total += val
    
    return total/len(values)


def median(values):
    values.sort()
    if len(values) % 2 == 0:
        #even
        return (values[(len(values)-2)//2] + values[(len(values))//2]) / 2
    else:
        #odd
        return values[(len(values)-1)//2]


def std_dev(values):
    x_bar = mean(values)
    n = len(values)

    dev_sum = 0
    for x in values:
        dev_sum += (x - x_bar) ** 2
    
    return sqrt(dev_sum / (n - 1))

def pop_std_dev(values):
    x_bar = mean(values)
    n = len(values)

    dev_sum = 0
    for x in values:
        dev_sum += (x - x_bar) ** 2

    return sqrt(dev_sum / (n))


def chebychev(values, k):
    x_bar = mean(values)
    dev = std_dev(values)

    values.sort()
    count = 0
    for val in values:
        if val >= x_bar - k * dev:
            if val <= x_bar + k * dev:
                count+= 1
            else:
                break

    approx = 100 * (1 - 1/(k**2))
    actual = 100 * count / len(values)
    return (approx, actual)


def sortNums(values):
    values.sort()
    with open("out.txt","w") as output:
        for val in values:
            print(val, file=output)


def quartiles(values):
    values.sort()
    Q2 = median(values)
    
    bot = []
    top = []
    i = 0

    while values[i] < Q2:
        bot.append(values[i])
        i += 1
    while i < len(values):
        top.append(values[i])
        i += 1

    Q1 = median(bot)
    Q3 = median(top)

    return (Q1, Q2, Q3)

def summary(values):
    qt = quartiles(values)
    return (min(values), qt[0], qt[1], qt[2], max(values))

if __name__ == "__main__":
    if len(argv) < 3:
        print("Invalid syntax.\n"
              + "Options: mean...")
        exit()
    if argv[2] == "-f":
        with open(argv[3],"r") as file:
            newargs = file.read().split("\n")
    else:
        newargs = argv[2:]

    numbify(newargs)
    if   argv[1] == "mean":
        print("Mean of {} values: {}".format(len(newargs), mean(newargs)))
    elif argv[1] == "median":
        print("Median of {} values: {}".format(len(newargs), median(newargs)))
    elif argv[1] == "sum":
        print("Sum of {} values: {}".format(len(newargs), sum(newargs)))
    elif argv[1] == "range":
        print("Range of given sample: {}".format(max(newargs) - min(newargs)))
    elif argv[1] == "stddev":
        print("Standard deviation of given sample: {}".format(std_dev(newargs)))
    elif argv[1] == "popstddev":
        print("Population standard deviation of given sample: {}".format(pop_std_dev(newargs)))
    elif argv[1] == "chev":
        k = float(input("How many deviations are you checking within? "))
        result = chebychev(newargs, k)
        print("{}% observations lie within {} standard deviations of the mean".format(result[1], k))
    elif argv[1] == "sort":
        sortNums(newargs)
        print("Result output to out.txt")
    elif argv[1] == "quart":
        result = quartiles(newargs)
        print("Quartiles of the given set...\n  "
              + "Q1 = {}\n  Q2 = {}\n  Q3 = {}".format(result[0], result[1], result[2]))
    elif argv[1] == "summary":
        result = summary(newargs)
        print("Summary of the data set: ", end=" ")
        for val in result:
            print(val, end=", ")
        print()
    else:
        print("Not a recognized option.")