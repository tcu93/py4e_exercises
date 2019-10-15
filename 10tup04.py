directory = dict()
first = 'chris'
last = 'gidden'
number = 2

directory[last, first] = number

print(number)

for last, first in directory:
    print(first, last, directory[last,first])