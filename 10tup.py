print("")
 
#  return list of tuples, where each tuple is a key-value pair
d = {'b':10, 'a':1, 'c':22}
t = list(d.items())  # list the items of d
t.sort() # sorts by key
print(t) # [('a', 1), ('b', 10), ('c', 22)]

print("")

# traverse the keys and values of a dictionary in a loop
for k, v in list(d.items()):
    print(v, k)  # notice printed value first
    # 10 b
    # 1 a
    # 22 c

print("")

for k, v in t:
    print(v, k) 
    # 1 a
    # 10 b
    # 22 c

