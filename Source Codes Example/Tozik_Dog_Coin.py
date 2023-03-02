all_coins = int(input("Coins : "))
people = int(input("People : "))

while all_coins > people:
    all_coins -= people

print(all_coins)