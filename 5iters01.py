

def min(x):
    smallest = None
    for value in x:
        if smallest is None or value < smallest:
            smallest = value
            print(smallest)
    return smallest

values = [55, 7, 9, 3, 44, 1, 88]

print(min(values))
