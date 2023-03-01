number = int(input("Enter Number K: "))
counter = 0
divider = 1
sw = False
while True:
    counter = 0
    for i in range(1,divider+1):
        # print(i,divider)
        if divider % i == 0:
            counter += 1
            
        if counter == number:
            sw = True
            break
    if sw:
        break
    divider += 1
    


print(divider)
