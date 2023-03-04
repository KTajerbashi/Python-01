def IsAval(number):
    counter = 2
    if number == 1 or number == 2 or number == 3:
        return True
    while counter < (number/2+2):
        if number % counter == 0:
            return False
        counter += 1
    return True

def Reverse(number):
    reversed = 0
    reminder = 0
    while number > 0:
        reminder = int(number % 10)
        reversed = (reversed * 10) + reminder
        number = int(number/10)
         
    return reversed

number = int(input("Enter Number : "))

while number > 0:
    # print(f"Your Number is {number} is {IsAval(number)}")
    if IsAval(number) and IsAval(Reverse(number)):
        print(f"Your Number is {number} Aval and Reverse is Is Aval")
    else:
        print(f"Your Number is {number} Not Aval")
        
    number = int(input("Enter Number : "))
    
        