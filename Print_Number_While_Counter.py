number = int(input("Enter Your Number: "))
remain = 0
while True:
    remain = int(number%10)
    number = int(number / 10)
    print(str(remain)*remain)
    if number <= 0 :
        break