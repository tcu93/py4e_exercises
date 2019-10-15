import string

fhand = open('romeo-full.txt')
dict1 = dict()

for line in fhand:

    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1

# Sort the dictionary by value
lst = list()

for k, v in list(dict1.items()):
    lst.append((v, k))

lst.sort(reverse=True)
print(lst)

# for k, v in the first 10 elements of lst
# everything up to, but not including, the 10th
for k, v in lst[:10]:
    print(k, v)
