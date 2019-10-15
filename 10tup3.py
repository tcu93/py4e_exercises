import string

fhand = open('mbox-short.txt')
dict1 = dict()

for line in fhand:

    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    words = line.split()

#create dict to store letter, letter counts

    #for word in words:
     #   if dict1

print(words)    