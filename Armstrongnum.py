def is_armstrong(number):
    num_str=str(number)
    num_digits=len(num_str)
    armstrong_sum=sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum==number
number=153
if is_armstrong(number):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not an armstrong number") 