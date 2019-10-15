print("")

# tuple assignment

m = ['have', 'fun']
x, y = m
print(x)  # roughly translates to print(m[0])
# have

n = ['this', 'is', 'now']
a, b, c = n
print(b) # is

# can swap values of variables
print(a) # this
print(c) # now
a, b, c = c, b, a
print(a) # now
print(c) # this

# right side can be any kind of sequence (string, list, tuple)
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, domain)



