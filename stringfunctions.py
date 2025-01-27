def string_builtin_function():
    sample_string="Hello, Python!"
    print("1. Length of the string(length): ",len(sample_string))
    print("\n2. Convert to Lowercase: ",sample_string.lower())
    print("\n3. Convert to Uppercase: ",sample_string.upper())
    print("\n4. Remove Leading and Trailing spaces(strip): ",sample_string.strip())  
    print("\n5. Split the string into a list(split): ",sample_string.split())
    print("\n6. Join a list into a string(join)")
    words=['Hello', 'Python']
    print("Joined: ", ", ".join(words))  
    print("\n7. Replace a substring(replace): ",sample_string.replace("Python","world"))  
    print("\n8. Find the position of a substring: ",sample_string.find("Python"))
    print("\n9. Count occurences of a substring: ",sample_string.count('o'))     
if __name__=="__main__":
    string_builtin_function()                      