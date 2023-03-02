def call_function(skill,callback):
    return (f"Your Skill is {skill} {callback}")

def information(name,family,*scores):
    sum_number = 0
    for score in scores:
        sum_number += score
    return (f"Hello {name} {family} your score is {sum_number}")


def more_information(info,*args,**kwargs):
    print(info)
    
    for item in args:
        print(f"Your args item is {item}")
    
    for k,v in kwargs.items():
        print(f"Your kwargs item is {k} : {v}")
    
    return "finished"

skill = input("Enter Skill : ")
name = input("Enter Name : ")
family = input("Enter Family : ")

print(call_function(skill,information(name,family,12,15,18,27)))
print(more_information(call_function(skill,information(name,family,12,15,18,27)),"Kaihan","Behnam","Sardar",kage=23,age=25,sage=28))