import random
import math

for i in range(10):
    x = random.random()
    print(x)
    
############################

y = random.randint(5, 19)
print(y)

############################

t = [1, 2, 3]
z = random.choice(t)
print(z)

###########################

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
print('\n')
print_lyrics()

##########################

def print_x(x):
    print(x)
    print(x)

print_x(round(math.pi,2))

#########################

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(4,5)
print(x)
