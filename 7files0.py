fhand = open('mbox-short.txt')
count = 0
'''
# count num of lines in file
for line in fhand:
    count += 1
print(f'Num Lines in File: {count}')
'''


for line in fhand:
    line = line.rstrip() # strip off \n character (removes spaces in output)
    if line.startswith('From:'): # print out lines which started with the prefix “From:”
    #if line.find('@uct.ac.za') == -1: # skip lines wo search param (-1)
       # continue
       count += 1
       print(count)
       print(line)