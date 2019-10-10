'''Exercise 4: Add code to the above program to figure 
out who has the most messages in the file. After all the 
data has been read and the dictionary has been created, 
look through the dictionary using a maximum loop (see 
Chapter 5: Maximum and minimum loops) to find who has the
most messages and print how many messages the person has.'''

fhand = open('mbox-short.txt')

dict1 = dict()

maximum = 0
maximum_address = ''

# for each line in file
for line in fhand:

    words = line.split()

    if not line.startswith('From') or len(words) < 3:
    #if len(words) < 3 or words[0] != 'From':
        continue
    else:
        # if dict1 does not have key = to words[1]
        if words[1] not in dict1:
            # dict value = value for that key
            dict1[words[1]] = 1
        else:
            # dict value = value + 1 for that key
            dict1[words[1]] += 1

print(dict1)

for val in dict1:
    if dict1[val] > maximum:
        maximum = dict1[val]
        maximum_address = val

print(maximum_address, maximum)


'''# Better solution using lambda - insert in for loop
# compare items in dict1 based on their [1]st element
x = max(dict1.items(), key=lambda k: k[1])
print(x)
'''

