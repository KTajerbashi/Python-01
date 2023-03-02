def check_reminder(number, i):
    return number % i;

number = int(input("Enter a number : "))
counter = 1
remain = 0
while number >= counter:
    print(f"Number : {number} remain on {counter} is {check_reminder(number, counter)}")
    if check_reminder(number,counter) >= remain:
        remain = counter
    counter += 1
    
print(f"Result : {remain}")