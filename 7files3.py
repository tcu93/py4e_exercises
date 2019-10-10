'''
Modify the program that prompts the user for the file 
name so that it prints a funny message when the user 
types in the exact file name ’na na boo boo’. The 
program should behave normally for all other files which 
exist and don’t exist.
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