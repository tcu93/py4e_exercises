n = 5

while n > 0:
    print(n)
    n -= 1
print('blastoff')

######################
'''
if precede text with # it will do nothing
otherwise it just parrots what you type
if you type done it will break & print Done
'''
'''while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')'''

######################

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print(f'Happy New Year: {friend}')
print('Done!')

######################

largest = None
num_list = [3, 41, 55, 34, 9, 77]

for num in num_list:
    if largest is None or num > largest:
        largest = num
    print(f'Loop: {num} Largest: {largest}')
print(f'Largest: {largest}')

###### or #######


######################

