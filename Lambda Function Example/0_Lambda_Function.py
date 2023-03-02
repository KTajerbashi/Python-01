def func_n(n):
    def func_x(x):
        return x * n
        
    return func_x
    
x = func_n(10)

print(x(2))


def func_n_lambda(x):
    return lambda n: x * n

lambda_func_1 = func_n_lambda(20)

print("Result : ",lambda_func_1(2))