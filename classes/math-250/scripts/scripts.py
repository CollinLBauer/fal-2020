from sys import argv
from math import sqrt

OPTIONS = ["mean", "median", "sum", "range", "sstddev", "pstddev", "chev", "sort", "quart", "summary", "rstddev"]
EXPECTED_USAGE = "Expected usage: python3 scripts.py <option> [-f <filename>|[arguments]]"

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


# Sample Standard Deviation
def std_dev(values):
    x_bar = mean(values)
    n = len(values)

    dev_sum = 0
    for x in values:
        dev_sum += (x - x_bar) ** 2
    
    return sqrt(dev_sum / (n - 1))


# Population Standard Deviation
def pop_std_dev(values):
    x_bar = mean(values)
    n = len(values)

    dev_sum = 0
    for x in values:
        dev_sum += (x - x_bar) ** 2

    return sqrt(dev_sum / (n))


# Random Variable Standard Deviation
def rnd_std_dev(values):
    print("Note: This function expects values in pairs of x and P(X = x).")
    if len(values) % 2 != 0:
        print("Invalid values length. Exiting.")
        exit()

    # find mu
    mu = 0
    for i in range(len(values)//2):
        mu += values[2*i] * values[2*i+1]

    #find summation
    dev_sum = 0
    for i in range(len(values)//2):
        # x = values[2*i]
        # P(P=x) = values[2*i+1]
        dev_sum += (values[2*i] - mu)**2 * values[2*i+1]

    return sqrt(dev_sum)


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


def sort_nums(values):
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


def __list_options__():
    printStr = "Available options...\n"
    for option in OPTIONS:
        printStr += "  " + option + "\n"
    print(printStr)


if __name__ == "__main__":
    # catch invalid usage cases
    if len(argv) < 2:
        print(EXPECTED_USAGE)
        exit()
    elif argv[1] == "help":
        print(EXPECTED_USAGE)
        __list_options__()
        exit()
    elif argv[1] not in OPTIONS:
        print("Not a recognized option.")
        __list_options__()
        exit()
    elif len(argv) == 2:
        print("No arguments passed.\n"
        + EXPECTED_USAGE)
        exit()

    # read in arguments as numbers
    if argv[2] == "-f":
        with open(argv[3],"r") as file:
            newargs = file.read().split()
    else:
        newargs = argv[2:]
    numbify(newargs)

    # run script based on selected option
    if   argv[1] == OPTIONS[0]:
        print("Mean of {} values: {}".format(len(newargs), mean(newargs)))
    
    elif argv[1] == OPTIONS[1]:
        print("Median of {} values: {}".format(len(newargs), median(newargs)))
    
    elif argv[1] == OPTIONS[2]:
        print("Sum of {} values: {}".format(len(newargs), sum(newargs)))
    
    elif argv[1] == OPTIONS[3]:
        print("Range of given sample: {}".format(max(newargs) - min(newargs)))
    
    elif argv[1] == OPTIONS[4]:
        print("Standard deviation of given sample: {}".format(std_dev(newargs)))
    
    elif argv[1] == OPTIONS[5]:
        print("Population standard deviation of given sample: {}".format(pop_std_dev(newargs)))
    
    elif argv[1] == OPTIONS[6]:
        k = float(input("How many deviations are you checking within? "))
        result = chebychev(newargs, k)
        print("{}% observations lie within {} standard deviations of the mean".format(result[1], k))
    
    elif argv[1] == OPTIONS[7]:
        sort_nums(newargs)
        print("Result output to out.txt")
    
    elif argv[1] == OPTIONS[8]:
        result = quartiles(newargs)
        print("Quartiles of the given set...\n  "
              + "Q1 = {}\n  Q2 = {}\n  Q3 = {}".format(result[0], result[1], result[2]))
    
    elif argv[1] == OPTIONS[9]:
        result = summary(newargs)
        print("Summary of the data set: ", end=" ")
        for val in result:
            print(val, end=", ")
        print()

    elif argv[1] == OPTIONS[10]:
        print("Random standard deviation of given pairs: {}".format(rnd_std_dev(newargs)))

    # Done
