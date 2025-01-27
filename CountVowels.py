def count_vowels():
    str=input("Enter a string: ")
    count=0
    vowels='aeiouAEIOU'
    for char in str:
        if char in vowels:
            count+=1
    print("The Number of vowels are: ",count)
count_vowels()    











