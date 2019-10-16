'''Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''

import string

fhand = open('romeo-full.txt')
dict1 = dict()
rel_list = list()
counts = 0

for line in fhand:

    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    words = line.split()
    
    for word in words:
        for letter in word:
            #print(letter)
            counts += 1
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1

# create sorted dictionary as list
sorted_dict1 = sorted(dict1.items()) 

print(sorted_dict1)

# create new list to hold sorted dict1 items
for k,v in sorted_dict1:
    rel_list.append((v / counts * 100, k))

rel_list.sort(reverse=True)

for k, v in rel_list:
    #print(v, round(k, 2))
    print(f'Letter: {v}  Frequency: {round(k, 3)}%')
 