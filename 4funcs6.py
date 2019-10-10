'''
Rewrite your pay computation with time-and-a-half for 
overtime and create a function called computepay which 
takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

def computepay(y, z):
    x = y * z
    return x

#inp = input('Enter Hours: ')
#hours = float(inp)
#inp = input('Enter Rate: ')
#rate = float(inp)

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    #a = computepay(hours, rate) * 1.05
    #print(a)
    print('Pay: ', computepay(hours, rate) * 1.05)
else:
    print('Pay: ', computepay(hours, rate))
