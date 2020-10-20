def secret():
    print("This is a brute force for Lab 8's secret problem.\n")
    with open("secret.txt","r", encoding="utf-8") as file:
        message = file.read()
        for i in range(40,80):
            newMessage = ""
            for char in message:
                newMessage += chr(ord(char)-i)

            print(-i, newMessage + "\n")

secret()