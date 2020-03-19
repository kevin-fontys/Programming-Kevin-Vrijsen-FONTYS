import string
import random

def passwordgenerate():
    password = ""
    option = 0
    lenght = int(input("insert the prefered length of your password?"))
    uppercase = input("do you want to use capital letters? (voer yes of no in)")
    if uppercase.lower() == "no":
        uppercase = False
    else:
        uppercase = True
    numbers = input("do you want to use numbers? (yes of no)")
    if numbers.lower() == "no":
        numbers = False
    else:
        numbers = True
    symbols = input("do you wan't to use symbols? (yes of no)")
    if symbols.lower() == "no":
        symbols = False
    else:
        symbols = True

    if uppercase == False and numbers == False and symbols == False:
        option = 1
    elif uppercase == False and numbers == False and symbols == True:
        option = 2
    elif uppercase == False and numbers == True and symbols == False:
        option = 3
    elif uppercase == True and numbers == False and symbols == False:
        option = 4
    elif uppercase == False and numbers == True and symbols == True:
        option = 5
    elif uppercase == True and numbers == False and symbols == True:
        option = 6
    elif uppercase == True and numbers == True and symbols == False:
        option = 7
    elif uppercase == True and numbers == True and symbols == True:
        option = 8
    else:
        print("oops, something went wrong there, please follow the steps and answer correctly.")
    for i in range(0, lenght):
        if option == 1:
            password = password + random.choice(string.ascii_lowercase)
        elif option == 2:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.ascii_letters) + str(string.digits)
            password = password + str(randomchoise)
        elif option == 3:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.punctuation) + str(string.ascii_letters)
            password = password + str(randomchoise)
        elif option == 4:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.punctuation) + str(string.ascii_lowercase) + str(string.digits)
            password = password + str(randomchoise)
        elif option == 5:
            password = password + random.choice(string.ascii_letters)
        elif option == 6:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.digits) + str(string.ascii_lowercase)
            password = password + str(randomchoise)
        elif option == 7:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.punctuation) + str(string.ascii_lowercase)
            password = password + str(randomchoise)
        elif option == 8:
            randomchoise = random.choice(optionlist)
            optionlist = str(string.punctuation) + str(string.ascii_letters) + str(string.digits)
            password = password + str(randomchoise)
        else:
            password = ""
    print(password)

passwordgenerate();
