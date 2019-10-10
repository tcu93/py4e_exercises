import string

fname = input('Enter the file name: ')
try:
    f = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

dict1 = dict()

for line in f:
    line = line.rstrip()
    # replace '' with '' (nothing), delete all punctuation
    line = line.translate(line.maketrans('', '', string.punctuation))
    # remove capital letters
    line = line.lower()
    # create list
    words_list = line.split()
    # for each word in words[]
    for word in words_list:
        # if word not already in words[]
        if word not in dict1:
            '''dict1[word] = 1
        else:
            dict1[word] += 1'''
            # add it to dict1{} & increment it's value by 1
            dict1[word] = dict1.get(word, 0) + 1

print(dict1)
