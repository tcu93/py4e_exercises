'''
Exercise 4   Download a copy of the file from www.py4inf.com/code/romeo.txt
Write a program to open the file romeo.txt and read it line by line. For 
each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is 
not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical 
order.

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 
'and', 'breaks', 'east', 'envious', 'fair', 'grief', 
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 
'sun', 'the', 'through', 'what', 'window', 
'with', 'yonder']
'''

from urllib.request import urlopen

url = 'http://www.py4inf.com/code/romeo.txt'

data = urlopen(url)

str_list = []

for line in data:
    str = line.decode()
    ss = str.split()

    for x in ss:
        if x not in str_list:
            str_list.append(x)
            str_list.sort()

print(str_list)
