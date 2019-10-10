'''
Exercise 5   Write a program to read through the mail box data and when 
you find line that starts with “From”, you will split the line into words 
using the split function. We are interested in who sent the message which 
is the second word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From 
line and then you will also count the number of From (not From:) lines and 
print out a count at the end.

This is a good sample output with a few lines removed:

stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
...
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
27
'''
count = 0
f = open('mbox-short.txt')

# for each line in file
for line in f:
    # increment counter
    count += 1
    # remove newline at end of each line
    line = line.rstrip()

    # if line doesn't start with 'From', skip over it
    if not line.startswith('From '): 
        count -= 1
        continue

    # split line (sentence) into a list
    words = line.split()

    # print elements of new list
    #print(words)
    print(words[1])

print(count)