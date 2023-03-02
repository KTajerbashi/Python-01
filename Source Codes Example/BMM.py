#الگوریتمی بنویسید که با گرفتن دو عدد ب.م.م آنها را برگرداند.

number1=int(input("Enter the number1 : "))
number2=int(input("Enter the number2 : "))

while number1 != number2:
    if number1 > number2:
        number1 -= number2
    else:
        number2 -= number1
        
print("B.M.M Number is : " , number1)
    