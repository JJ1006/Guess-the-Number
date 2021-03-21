
import random
x=random.randint(1,11)

while True:
    try:
        y=int(input("\nPlease enter the guessed number : "))
    except ValueError:
        print("\nPlease enter an integer : ")
        continue

    if(y>x):
        print("\nThe actual number is smaller!!!")
    elif(y<x):
        print("\nThe actual number is greater!!!")
    elif(y==x):
        print("\nCONGRATULATIONS, you guessed the number correctly!!!\n")
        break




