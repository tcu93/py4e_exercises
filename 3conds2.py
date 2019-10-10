'''
Rewrite your pay program using try and except so that 
your program handles non-numeric input gracefully by 
printing a message and exiting the program. The following 
shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''

inp = input('Enter Hours:\n')

try:
    hours = float(inp)
    rate = 10.0
    pay = hours * rate
    if hours > 40:
        print(pay * 1.05)
    else:
        print(pay)
except:
    print('Error: Please re-run program & enter numeric input')

