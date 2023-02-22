import os

try:
    f = open("file1.txt", "r")
    for word in f.readlines():
        print(word)
except:
    print("File not found")
finally:
    f.close()
