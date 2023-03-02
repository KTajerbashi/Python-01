n = int(input("Enter N : "))
m = int(input("Enter M : "))
rangNumber = n * 2
dev = 0
result = 0
counter = 1
j = 0
# Near To N for Devided on M

while result <= (n+m):
    result = m * counter
    counter += 1
    dev = n - result
    dev = dev if dev > 0 else dev * -1
    if dev <= rangNumber and j<result:
        rangNumber = dev
        j=result


print("Result : ", j)