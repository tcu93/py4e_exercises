'''print the ten most common words in romeo-full.txt
'''

import string

fhand = open('romeo-full.txt')
dict1 = dict()

for line in fhand:
    # strip punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    # lower word tense
    line = line.lower()
    # create list()
    words = line.split()
    # loop thru list
    for word in words:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1

lst = list()

# populate list of tuples from dictionary
for k, v in list(dict1.items()):
    # append value first so it's used for sort (below)
    lst.append((v, k))

# reverse sort list so highest 10 values first
lst.sort(reverse=True)

# loop thru list & print key & value
for k, v in lst[:10]:
    print(k,v)

