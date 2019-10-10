'''There is a string method called count that is similar 
to the function in the previous exercise. Read the 
documentation of this method at docs.python.org/library/string.html 
and write an invocation that counts the number of times the letter 
a occurs in 'banana'.
'''

word = 'banana'
x = word.count('a')
print(x)

# data.find()
# find position of @ sign
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# Find position of first space after the @ sign
# Find first space starting at atpos (21)
sppos = data.find(' ', atpos)  # data.find('char_to_find', start, end)
print(sppos)
# Use string slicing to extract the portion of the string we're looking for
# starts at 22 & goes to 31
host = data[atpos+1:sppos]
print(host)