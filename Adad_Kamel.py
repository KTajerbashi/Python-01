#الگوریتمی بنویسید که عددي را از ورودي خوانده و مشخص کند که ایا کامل هستند یا خیر.(عدد کامل به عددي گفته میشود که مجموع مقسوم علیه هاي ان عدد بجز خودش، برابر با خودش شود.).

number=int(input("Enter a Number to Check : "))
Total=0
for i in range(1,number):
    if number%i == 0:
        Total += i

if Total == number:
    print("This is a Kamel Number")
else:
    print("This is not a Kamel Number")