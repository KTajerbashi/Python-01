#الگوریتمی بنویسید که یک عدد را دریافت و وارون آن را محاسبه و بهمراه خود عدد چاپ کند. مثال وارون عدد 3872 برابر 2783 می باشد.

number = int(input("Enter a number : "))

Reminder = 0
Reverse = 0
n = number

while n != 0 :
    Reminder = n%10
    Reverse = ( Reverse * 10 ) + Reminder 
    n = int(n / 10)

print("Number  : " , number)
print("Reverse : " , Reverse)