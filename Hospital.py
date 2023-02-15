

class doctor:
    def __init__(self, Id, name, family, degree, workTime, hrSalary, inWorkH, outWorkH, totalSalary, totalWorkTime):
        self.Id = Id
        self.Name = name
        self.Family = family
        self.Degree = degree
        self.WorkTime = workTime
        self.hrSalary = hrSalary
        self.inWorkH = inWorkH
        self.outWorkH = outWorkH
        self.totalSalary = totalSalary
        self.totalWorkTime = totalWorkTime
        

list_doctors=[]

def ShowOption():
    print("-------------------------------------------")
    print("--------------   Hospital    --------------")
    print("-------------------------------------------")
    print("0 : Exit Application")
    print("1 : Register New")
    print("2 : Show By ID")
    print("3 : Delete By ID")
    print("4 : Update By ID")
    print("5 : Control Work Time")
    print("6 : Control Salary")
    print("7 : Register New")
    print("8 : Register New")
    print("9 : Register New")
    print("10 : Register New")



def Register():
    print("Starting Register")
    
    
ShowOption()

while True:
    userSection=int(input("Select : "))
    if userSection == 0:
        print("God Buy")
        break
    elif userSection == 1:
        print("-------------------------------------------")
        print("----------   Register Option     ----------")
        print("-------------------------------------------")
    elif userSection == 2:
        print("-------------------------------------------")
        print("------   Show information Option     ------")
        print("-------------------------------------------")
    elif userSection == 3:
        print("-------------------------------------------")
        print("-----------   Delete Option     -----------")
        print("-------------------------------------------")
    elif userSection == 4:
        print("-------------------------------------------")
        print("-----------   Update Option     -----------")
        print("-------------------------------------------")
    elif userSection == 5:
        print("-------------------------------------------")
        print("------   Control Work Time Option    ------")
        print("-------------------------------------------")
    elif userSection == 6:
        print("-------------------------------------------")
        print("-------   Control Salary Option     -------")
        print("-------------------------------------------")
    elif userSection == 7:
        print("-------------------------------------------")
        print("----------   Register Option     ----------")
        print("-------------------------------------------")
    elif userSection == 8:
        print("-------------------------------------------")
        print("----------   Register Option     ----------")
        print("-------------------------------------------")
    elif userSection == 9:
        print("-------------------------------------------")
        print("----------   Register Option     ----------")
        print("-------------------------------------------")
    elif userSection == 10:
        print("-------------------------------------------")
        print("----------   Register Option     ----------")
        print("-------------------------------------------")    
    else:
        ShowOption()
else:
    print("-----    Application is Disabled -----")
