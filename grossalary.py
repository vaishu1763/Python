basic_salary=float(input("Enter the basic salary: "))
hra=0.60*basic_salary
da=0.20*basic_salary
ta=0.05*basic_salary
gross_salary=hra+da+ta
print("Gross salary is: ",gross_salary)