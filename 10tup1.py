fhand = open('mbox-short.txt')

dict1 = dict()

# for each line in file
for line in fhand:

    words = line.split()

    if not line.startswith('From') or len(words) > 2:
        continue
    else:
        # print(words)
        if words[1] not in dict1:
            dict1[words[1]] = 1
        else:
            dict1[words[1]] += 1

# print(dict1)

# Sort the dictionary by value
t = list()

for k, v in list(dict1.items()):
    t.append((v, k))

t.sort(reverse=True)
#print(lst)

# for k, v in the first 1 elements of lst
# everything up to, but not including, the 1st
for k, v in t[:1]:
    print("")
    print(v, k)



