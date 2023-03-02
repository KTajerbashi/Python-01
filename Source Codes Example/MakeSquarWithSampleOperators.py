#الگوریتمی بنویسید که یک عدد را از ورودی خوانده و با استفاده از 4 عمل اصلی جذر آن را حساب کند.

number = int(input("Enter Your Number : "))

for i in range(1,int(number/2)):
    if i*i==number:
        print("Square Number is : ",i)
        break;
    elif i*i>number:
        print(number," don't have a square number")
        break;
        

        
