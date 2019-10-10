fhand = open('mbox-short.txt')
#count = 0

# Write a program to read through a file and print 
# the contents of the file (line by line) all in upper case
for line in fhand:
    line = line.upper()
    print(line)