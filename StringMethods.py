def string_Methods():
    str=input("Enter a string: ")
    print("Is alphanumeric: ",all(c.isalnum() for c in str))
    print("Is alphabetic: ",all(c.isalpha() for c in str))
    print("Is Upper: ",str.isupper())
    print("Is lower: ",str.islower())
    print("Is digit:  ",str.isdigit())
    print("is space: ",all(c.isspace() for c in str))
string_Methods()