print("")
# create tuple from string
x = tuple('lupins')
print(x, '\n')

###################################################
txt = 'but soft what light in yonder window breaks'
t = list()
words = txt.split()
for word in words:
    # create a list of tuples [(word, len(word)), ...]
    t.append((word, len(word)))
    # t[0][1] = 'yonderful'    # this would fail due to immutability

t.sort(reverse=True)
#t.sort() # or reverse
print(f't = {t}\n')

res = list()
# loop thru each tuple in t
for word, length in t:  
    # append to list (res) - sorted by length
    res.append(length)
    # res.sort()

print(f'res = {res}\n')
###################################################

