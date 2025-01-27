def Exception_Handling():
    try:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print("Division: ",num1/num2)
    except ZeroDivisionError:
        print("Error: cannot be divided by zero")
    except ValueError:
        print("Error: Invalid input")
Exception_Handling()