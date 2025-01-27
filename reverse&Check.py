def is_palindrome(number):
    original_number=number
    reversed_number=0
    while number>0:
        rem=number%10
        reversed_number=reversed_number*10+rem
        number=number//10
    if original_number==reversed_number:
        return True
    else:
        return False
number=int(input("Enter a number: "))
if is_palindrome(number):
    print("The number is palindrome")
else:
    print("The number is not palindrome")        
is_palindrome(number)