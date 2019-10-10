'''Exercise 3: Write a program to read through a mail log, 
build a histogram using a dictionary to count how many messages 
have come from each email address, and print the dictionary.
'''

fhand = open('mbox-short.txt')

dict1 = dict()

# for each line in file
for line in fhand:
    words = line.split()

    # < 3 because words contains 2-element-only lists we dont want
    if not line.startswith('From') or len(words) < 3:
        continue
    else:
        print(words)
        if words[1] not in dict1:
            dict1[words[1]] = 1
        else:
            dict1[words[1]] += 1

print(dict1)

#print(words)