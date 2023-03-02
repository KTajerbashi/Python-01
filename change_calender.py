from colorama import *

print(Fore.RED,"*"*50)
print(Fore.YELLOW,("Change Calender").center(50))
print(Fore.RED,"*"*50)

def ShowChoices():
    print(Fore.GREEN,"-"*20)
    print("1 : Change Shamsi to Miladi")
    print("2 : Change Shamsi to Ghamary")
    print("3 : Change Miladi to Shamsi")
    print("4 : Change Miladi to Ghamary")
    print("5 : Change Ghamary to Miladi")
    print("6 : Change Ghamary to Shamsi")
    print("-"*20)
    return int(input("Enter Number : "))

def get_date():
    sw = True
    print(Fore.RED,"="*30)
    
    while sw:
        day = int(input("Enter Day : "))
        if day < 31 and day > 0:
            sw = False
    
    sw = True    
    while sw:
        month = int(input("Enter Month : "))
        if month < 13 and month > 0:
            sw = False
    
    sw = True
    while sw:
        year = int(input("Enter Year : "))
        if year < 3000 and year > 0:
            sw = False
    
    print(Fore.RED,"="*30)
    
    return (f"{year}/{month}/{day}")
    
def shamsi_to_miladi():
    date = get_date().split("/")
    print(date)
    if int(date[1]) <= 10 and int(date[2]) <= 10:
        return (f"Your Date is : {int(date[0])+621}")
    else: 
        return (f"Your Date is : {int(date[0])+622}")

if ShowChoices() == 1:
    print(Fore.GREEN,Back.WHITE,shamsi_to_miladi())
    print(Fore.YELLOW,Back.BLACK,"$"*50)
elif ShowChoices() == 2:
    pass
elif ShowChoices() == 3:
    pass
elif ShowChoices() == 4:
    pass
elif ShowChoices() == 5:
    pass
elif ShowChoices() == 6:
    pass
else:
    print("Wrong Input")