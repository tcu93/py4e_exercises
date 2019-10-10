dic = {'A': 1, 'B': 2}

print(dic['A'])
# or #
print(dic.get('A'))

# print val of key 'C' - if not exist, print 'd'
print(dic.get('C', 'd')) 

########################################################

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
y = car.get("ajax", 'not a member')

print(x)
print(y)

########################################################


