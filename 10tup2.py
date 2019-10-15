fhand = open('mbox-short.txt')

dict1 = dict()
lst = list()

# for each line in file
for line in fhand:

    words = line.split()

    if not line.startswith('From') or len(words) < 4:
        continue
    
    col_pos = words[5].find(':') # returns numeric col pos: [2]
    hour = words[5][:col_pos] # sets 'hour' as words[5][2]

    if hour not in dict1: # if value of 'hour' not in dict1
        dict1[hour] = 1     
    else:
        dict1[hour] += 1    

for k, v in list(dict1.items()): # for each k,v combo in dict1
    # k = hour, v = count of hour
    lst.append((k, v))  # Fill list with hour, count of dict

lst.sort() # Sort by hour

for k, v in lst:
    print(k, v)