def is_perfect_num():
    num=int(input("enter a number:"))
    divisors_sum=sum(i for i in range(1,num) if num%i==0)
    if divisors_sum==num:
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not a perfect number")
is_perfect_num()