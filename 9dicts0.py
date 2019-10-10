# Create a dictionary by key/value index
dict1 = dict()
dict1['1'] = 'uno'
dict1['2'] = 'dos'
dict1['3'] = 'tres'
print(dict1)
print(dict1['2'])

# Create dict by variable assignment
dict2 = {'1': 'uno', '2': 'dos'}
print(dict2)

# Return num of key/value pairs
print(len(dict2))

# Key, not value
if '1' in dict2:
    print('True')
if 'uno' in dict2:
    print('True')

# Create list from Dictionary values or keys
dict_lst = list(dict1.values())
print(dict_lst)
dict_lst1 = list(dict1.keys())
print(dict_lst1)

# Look through keys in dict
for keys in dict1:
    print(keys)

# Loop through values in dict
for values in dict1.values():
    print(values)

# get() to retrieve values for keys
'''Dict.get(key, default=None)'''

print(dict1.get('1', 0))

