#قطعه کدی بنویسید که با گرفتن یک عدد به عنوان ورودی مجموع ارقام آن را چاپ کند.

number=int(input("Enter the number : "))
mainNumber=number
total =0;
reminder =0;

while number != 0:
    reminder= number%10
    number /= 10
    total += reminder
    
print(f"Total number {mainNumber} is : ",int(total))