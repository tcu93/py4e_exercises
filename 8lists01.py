'''
a small program that looks for lines where the 
line starts with “From ” and then split those 
lines and then print out the third word in the line
'''

fhand = open('mbox-short.txt')
for line in fhand:

    # remove newline at end of file
    #line = line.rstrip()

    # if line doesn't start with 'From', skip over it
    if not line.startswith('From '): 
        continue

    # split line (sentence) into a list
    words = line.split()

    x = (len(words))

    # print elements of new list
    print(words)
    print(words[2])

