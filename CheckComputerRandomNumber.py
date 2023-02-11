import random
print("------------------")
print("-- Game started --")
print("------------------")
a=0
b=100
computerNumber=random.randint(a,b)
Check=input(f'Your Number is {computerNumber} ? \n(G) Greater\n(L) Less\n(E) Equal\n>>> : ')
print(type("g"))
print(type("G"))
print(type(Check))
while Check != "e" and Check!="E":
    if Check == "g" or Check == "G":
        a=computerNumber
        computerNumber=random.randint(a,b)
        print("Greater")
    elif Check == "l" or Check == "L":
        b=computerNumber
        computerNumber=random.randint(a,b)
        print("Less")
        
    Check=input(f'Your Number is {computerNumber} ? \n(G) Greater\n(L) Less\n(E) Equal\n>>> : ')
    
    

print("--------------------------------")
print(f'----------Your Number is {computerNumber} -----------')
print("--------------------------------")
