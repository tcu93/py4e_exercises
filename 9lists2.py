'''Exercise 2: Write a program that categorizes each mail 
message by which day of the week the commit was done. To 
do this look for lines that start with "From", then look 
for the third word and keep a running count of each of the 
days of the week. At the end of the program print out the 
contents of your dictionary (order does not matter).
'''

fhand = open('mbox-short.txt')

dict1 = dict()

# for each line in file
for line in fhand:

    # create words list
    words = line.split()

    # if line doesn't start with From, skip it
    if not line.startswith('From') or len(words) < 3:
        continue
    else:
        words1 = words[2]
        # remember, you start with an existing, empty dictionary
        if words1 not in dict1:
            dict1[words1] = 1
        else:
            dict1[words1] += 1

print(dict1)
# Print dict sorted by key (day of week) - can reverse it too
#print(dict(sorted(dict1.items(), reverse=True)))
