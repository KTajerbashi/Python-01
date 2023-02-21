#الگوریتمی بنویسید که با دریافت یک عدد مشخص کند که آن عدد کاملا اول است یا خیر . عددی کاملا اول است که : 1 خودش اول باشد 2 اگر از سمت راست آن عدد ، رقمی جدا کنیم , باز هم عدد باقی مانده اول باشد . مثلا 23 کاملا اول است چون 23 اول است و 2 نیز اول است . اگر عدد کاملا اول بود در خروجی 1 و در غیر این صورت 0 چاپ کند.
# A optimized school method based  
# Python3 program to check 
# if a number is prime 
  
  
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  

number = int(input("Enter a number : "))
if isPrime(number) :
    print(number)
    number /= 10
    print(int(number))
    if isPrime(int(number)) :
        print("1")
    else :
        print("Not Complete Prime Number")
else:
    print("0")
    