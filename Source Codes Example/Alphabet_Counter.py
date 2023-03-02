name = (input("Enter Name: ")).lower().strip().replace(" ", "")

# Model 1
counter = 0
alphbets = {}
for i in name:
    counter = 0
    for n in name:
        if i == n:
            counter += 1
    alphbets[i] = counter

for k,v in alphbets.items():
    print (name, "has", v, k)

print("#"*40)
# Model 2
list_alphabet = []

for i in name:
    if i not in list_alphabet:
        print(f"{name} has {name.count(i)} : {i}")
        list_alphabet.append(i)