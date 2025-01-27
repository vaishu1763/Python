from datetime import datetime
def dates(date1,date2):
    d1=datetime.strptime(date1,"%Y-%m-%d")
    d2=datetime.strptime(date2,"%Y-%m-%d")
    delta=d2-d1
    return abs(delta.days)
date1=input("Enter the date1: ")
date2=input("Enter the date2: ")
print(f"The days between {date1} nd {date2} is: {dates(date1,date2)} days.")