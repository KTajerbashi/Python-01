row = int(input("Enter Row : "))
column = int(input("Enter Column : "))
sw = True
line = ""
for i in range(1,row+1):
    if i%2 == 1:
        print("#"*column)
    else:
        if sw:
            line = " "*(column-1)
            print(line+"#")
            sw = False
        else:
            line = " "*(column-1)
            print("#"+line)
            sw = True
            
        