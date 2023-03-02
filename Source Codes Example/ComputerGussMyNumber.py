import random
print("------------------")
print("-- Game started --")
print("------------------")

myNumber=int(input("My Number : "))
count =0
while True:
    number=random.randint(0,100)
    count+=1
    if number == myNumber:
        print("WoOOOow! you are Win ! after ",count,"try it !")
        print("My Number : ",myNumber)
        print("Computer Number : ",number)
        break
    elif number > myNumber:
        print("My Number is Smaller")
    else:
        print("My Number is Biger")
        