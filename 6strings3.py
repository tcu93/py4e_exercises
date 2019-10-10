
word = 'banana'
letter_count = 0

for letter in word:
    if letter == 'a':
        letter_count += 1

print(letter_count)

'''
Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and 
the letter as arguments.
'''

def count(letter, word):
    l_count = 0
    for x in word:
        if x == letter:
            l_count += 1
    return l_count

l = input('Enter Letter: ')
w = input('Word: ')
v = count(l, w)
print(f'{l} occurs {v} times in the word {w}')

