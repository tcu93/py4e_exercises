'''
Exercise 4   Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression 
and the type (of the value of the expression).

width/2
width/2.0
height/3
1 + 2 * 5
'''

width = 17.344
height = 12.0

#a = width / 2
a = lambda w: w / 2
b = width / 2.0
c = height / 3
x = 1 + 2 * 5 

#print(round(a, 3))
print(round(a(width), 3))
print(round(b))
print(round(c, 2))
print(float(x))
