def warmup():
    myStr = input("Enter some string: ")

    print("a) " + myStr[0], myStr[-1])
    print("b) " + myStr[3:7])
    print("c) " + len(myStr))
    print("d) " + myStr[:3]*10)
    
    e = "e) "
    for char in myStr:
        e += char + ","
    print(e[:-1])

def my_len():
    

def main():
    warmup()
    my_len()

main()