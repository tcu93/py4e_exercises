'''
Search contents of a provided file
'''

fname = input('Enter file name:')
fterm = input('Enter search term:')

try:
    fhand = open(fname)
except:
    print(f'File {fname} cannot be opened')
    exit()


count = 0
for line in fhand:
    if line.startswith(fterm): # or whatever
        count += 1
print(f'{count} lines start with: "{fterm}"')