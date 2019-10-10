'''Exercise 5: This program records the domain name (instead of 
the address) where the message was sent from instead of who the 
mail came from (i.e., the whole email address). At the end of the 
program, print out the contents of your dictionary.
'''

fhand = open('mbox-short.txt')

dict1 = dict()

# for each line in file
for line in fhand:

    words = line.split()

    if not line.startswith('From') or len(words) > 2:
        continue
    else:
        # Find position of '@' in words[1]
        stpos = words[1].find('@')
        # Store rest of words[1] characters
        srch_str = words[1][stpos+1:]     
        #print(domain)
        if srch_str not in dict1:
            dict1[srch_str] = 1       
        else:
            dict1[srch_str] += 1      
    #print(words)

print(dict1)

