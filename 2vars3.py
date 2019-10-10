'''Exercise 3   Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
'''

crt_product = lambda arg1, arg2: arg1 * arg2

hours = int(input('Enter Hours: '))
rate = int(input('Rate: '))
#pay = hours * rate
#print(f'Pay: {pay}')
print('Pay:', crt_product(hours, rate))