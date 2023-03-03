# def print_number(x):
#     print("Your Number is :",x)
    
# map_fun = map(print_number,(1,2,4,5,8,45,12,13,48))
# print(list(map_fun))

# Lambda functions in Map

lambda_map_function = map(lambda x: x,(10,11,45,21,23,41,71,73,25))

print(list(lambda_map_function))

lambda_map_function2 = map(lambda x, y: x*y,(10,11,45,21,23,41,71,73,25),(13,10,15,26,18,44,56,58,15))

print(list(lambda_map_function2))