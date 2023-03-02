i = 1
m = 0
lastNumber = 0

m = int(input("M : "))
while m != -1:
    if i % 2 == 0:
        lastNumber += m
    else:
        lastNumber -= m
    
    i += 1
    m = int(input("M : "))
    
print("Result : ", lastNumber)
