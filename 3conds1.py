'''
Rewrite your pay computation to give the employee 
1.5 times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
hours = float(input('Enter Hours:\n'))
rate = 10.0
pay = hours * rate

if hours > 40:
    print(pay * 1.05)
else:
    print(pay)
