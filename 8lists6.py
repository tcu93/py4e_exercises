'''
Exercise 6: Rewrite the program that prompts the user for a 
list of numbers and prints out the maximum and minimum of the 
numbers at the end when the user enters "done". Write the 
program to store the numbers the user enters in a list and 
use the max() and min() functions to compute the maximum and 
minimum numbers after the loop completes.
'''

inp_lst = []

inp = ''

while inp != 'done':
    inp = input('Enter a number: ')
    inp_lst.append(inp)

if inp == 'done':
    inp_lst = inp_lst[:-1]
    print(inp_lst)
    print(max(inp_lst))
    print(min(inp_lst))
    
