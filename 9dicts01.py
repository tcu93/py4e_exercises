'''Suppose you are given a string and you want 
to count how many times each letter appears.'''

word1 = 'brontosaurus'
dict1 = dict()

# Create dict from string (word1)
for c in word1:  # for c'th element of word1
    dict1[c] = dict1.get(c, 0) + 1  # c'th elem of dict1 = value of that elem + 1

print(dict1)
print(dict1['r'])

''' 
THIS ALSO WORKS
for x in word1:
    y = x.split()
    if x not in dict1:  # confusing -- x acts as both letter & index at same time
        dict1[x] = 1  # this is value, no key
    else:
        dict1[x] += 1
'''

# Check for presence of particular key value
if 'b' in dict1:
    print('true')

# Create list of dict1 keys
keys = list(dict1.keys())
print(keys)

# Create list of dict1 values
vals = list(dict1.values())
print(vals)