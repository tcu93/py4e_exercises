#fname = input('Enter file name:')
from statistics import mean

fhand = open('mbox-short.txt')
lst = []

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        # Find line position of first occurrence of a '0'
        atpos = line.find('0')
        # Find line pos of 2nd to last element in line
        sppos = line.rindex('\n') - 1
        # store characters from point a to b in current line
        line = line[atpos:sppos]
        # Append characters to list
        lst.append(line)
# Convert list elements to type float
lst = list(map(float, lst))
# Print average of lst elements
print('Average spam confidence: ', round(mean(lst), 4))