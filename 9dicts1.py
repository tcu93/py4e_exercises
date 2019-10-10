
'''Loop through lines in file - assign each as key in dict - 
assign each key value of None
'''

f = open('words.txt')

# Create dictionary
dict1 = dict()

# Create list
words = list()

# Store contents of file
text = f.read()

# Populate list
words = text.split()

# Loop through list
# Populate keys of dict with each word in list
# Assign value of each key to None
for i in words:
    dict1[i] = None

print(dict1)