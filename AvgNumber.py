total=0
count=0

number = int(input("Enter number : "))
while number  != 0:
    total += number
    count += 1
    print(f'Input number is {number} count is {count} total is {total}')
    number = int(input("Enter number : "))

print("Total Sum: " , total)
print("Count: " , count)
print("Average: " , total/count)

    