data = 'X-DSPAM-Confidence:  0.8475'

atpos = data.find(' ')
print(atpos)

sppos = data.find('5')
print(sppos)

# move atpos 2 to right - sspos 1 to right to incl last char
word = float(data[atpos+2:sppos+1])
print(word)