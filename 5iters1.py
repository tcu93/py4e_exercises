from statistics import mean

ent_nums = []

while True:
    n = (int(input('Enter num: ')))
    if n >= 0:
        ent_nums.append(n)
    #print(f'List: {ent_nums}')

    try:
        print('Sum: ', sum(ent_nums))
        print('Avg: ', round(mean(ent_nums), 2))
        print('Count: ', len(ent_nums))
        print(max(ent_nums))
    except:
        if n == 'done':
            break
    '''while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')'''