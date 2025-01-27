def add_numbers(*args):
    total=sum(args)
    print("Sum of numbers is: ",total)
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
add_numbers(10,20,30,40)
student_info(name="vaishu",age=20,city="Warangal")