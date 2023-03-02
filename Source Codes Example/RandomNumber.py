import random

ComputerNumber = int(random.randint(1, 100))

print("----------------------------------------------------------------")
print("------                   Game Started                     ------")
print("----------------------------------------------------------------")
myNumber=int(input("Enter Number to fine computer Number:"))
while True:
    if(myNumber == ComputerNumber):
        print("You Win !!!")
        print("Computer Number is your number : ",myNumber)
        break
    elif(myNumber > ComputerNumber):
        print("Computer Number is less than your number")
    else:
        print("Computer Number is Greater than your number")
    print("\n----------------------------------------------------------------")
    myNumber=int(input("Enter Number to fine computer Number:"))
    
print("Computer Number is : ",ComputerNumber)
