lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]
lst4 = ['a', 'b', 'c']
lst5 = ['a', 'b', 'c', 'd', 'e', 'f']
for j in lst4:
    print(j)

double = lambda arg1: arg1 * 2

for i in range(len(lst1)):
    # lst1[i] = lst1[i] * 2
    lst1[i] = double(lst1[i])
    print(lst1[i])

##### LIST OPERATIONS
lst3 = lst1 + lst2
print(lst3)
##### 
a = lst1[1] * 2
print(a)
b = lst2[1] * 2
print(b)

##### LIST SLICES
c = lst2[1:3]
print(c)

##### LIST METHODS
# append num onto lst2
lst2.append(6)
print(lst2)

# extend lst2 with contents of lst1
lst2.extend(lst1)
print(lst2)

# sort elements of lst2
lst2.sort()
print(lst2)

# delete element by index
# if you don't provide index, will pop last elem
lst2.pop(4)
print(lst2)

# remove/delete element by value
lst4.remove('b')
print(lst4)
# utility
lst4.extend(lst1)
print(lst4)

# delete more than one element (consecutive)
del lst5[1:4]
print(lst5)

# remove multiple elements of list by index
lst6 = [11, 5, 17, 18, 23, 50] 
    # remove 11, 18, 23 
unwanted = [0, 3, 4] 
for ele6 in sorted(unwanted, reverse = True):  
    del lst6[ele6] 
print (lst6) 

# Misc
print(len(lst5)) # num elements in lst5
print(max(lst5)) # highest val in lst5

# create list from string
s = 'spam'
xy = list(s)
print(xy)

# string to list (split)
tt = 'now is the time for all good men'
ss = tt.split()
print(ss)
print(ss[2])
uu = 'spam-spam-spam'
delimiter = '-'
vv = uu.split(delimiter)
print(vv)

# list to string (join)
print('### list to string (join)')
ooo = ['pining', 'for', 'the', 'fjord']
delim2 = '='
ppp = delim2.join(ooo)
print(ppp)

# strip leading space from string
print('### strip leading space from string')
random_string = ' this is good'
rs2 = random_string.strip(' ')
print(rs2)
rs3 = random_string.replace('s', 'x')
print(rs3)

# return last x elements (create function)
print('### return last x elements (create function)')
def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)

# strip() 
print('### strip()')
orig = '  ###$ My header here'
print(orig.strip('# $ '))  # strips all instances of whatever chars in arg

