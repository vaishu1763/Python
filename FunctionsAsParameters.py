def apply_functions(func,value):
    return func(value)
def square(x):
    return x*x
number=int(input("Enter a number: "))
result=apply_functions(square,number)
print(f"The square of {number} is: {result}")