#قطعه کدی را بنویسید که یک عدد را از ورودی دریافت کند و تعیین کند که آیا عدد در دنباله فیبوناچی هست یا خیر.

a=1
b=1
temp=1
sw=False
print("-------------------- Start Project --------------------")
number=int(input("Enter a number to checked is Fibonachi : "))

while b<=number:
    a=b
    b=temp
    temp=a+b
    if number == temp:
        sw=True
        break

if sw==True:
    print("it is Fibonachi Number")
else:
    print("it's not Fibonachi Number")
    
print("--------------------  End Project  --------------------")