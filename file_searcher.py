'''
Search contents of a provided file
'''

fname = input('Enter file name:')
if fname == 'NA':
    print('yo!')
    exit()
    
try:
    fhand = open(fname)
except:
    print(f'File {fname} cannot be opened')
    exit()


count = 0
for line in fhand:
    if line.startswith('From:'): # or whatever
        count += 1
print(f'The file has {count} occurrences')