'''We will write a Python program to read through the lines 
of the file, break each line into a list of words, and then 
loop through each of the words in the line and count each word 
using a dictionary.'''

f = open('words.txt')

dict1 = dict()

text = f.read()

# Create list()
words = text.split()

# for each element in list
for k in words:
    # value of dict[k] = that value + 1
    dict1[k] = dict1.get(k, 0) + 1

print(dict1)

##############################
# Print keys (k) & their values if values > 4

# for keys in dict
for k1 in dict1:
    # if value of key >= 4
    if dict1.get(k1) >= 4:
        # print key & it's assoc value
        print(k1, dict1[k1])