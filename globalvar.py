counter=0
def increment_counter():
    global counter
    counter+=1
    print(f"Counter inside the function: {counter}")
print(f"Counter before function call: {counter}")
increment_counter()
print(f"Counter after function call: {counter}")    