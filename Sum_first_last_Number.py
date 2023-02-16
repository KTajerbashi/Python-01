#برنامه ای بنویسید که با گرفتن عدد n ، مجموع اولین و آخرین رقم آن را چاپ کند


number = int(input("Enter a number to sum first & last number : "))

first = 0
last = 0
counter = 1
while number != 0:
    first = number%10
    if counter == 1:
        last = number%10
    counter += 1
    number =int(number/10)
    print(number)
    

print("Your First Number : ",first)
print("Your Last Number : ",last)
print("Total Sum of Number : ",first+last)
