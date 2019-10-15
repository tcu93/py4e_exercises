name = input('Enter file name: ')
if len(name)<1:
    name = 'mbox-short.txt'
hand = open(name)
counts = dict()


for line in hand:
    if not line.startswith('From '):
        continue
    words = line.split(' ')
    words = words[6]
    #print(words.split(':'))
    hour = words.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1
for k,v in sorted(counts.items()):
     print(k,v)
for k,v in sorted(counts.items()):
    print(k,v)