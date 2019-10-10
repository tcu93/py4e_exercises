from statistics import mean

ent_nums = []

while True:
    n = input('Enter num: ')
    try:
        if int(n) >= 0:
            ent_nums.append(int(n))
    except:
        if n == 'done':
            break

print(f'List: {ent_nums}')
print('Sum: ', sum(ent_nums))
print('Avg: ', round(mean(ent_nums), 2))
print('Count: ', len(ent_nums))
print('Lowest: ', min(ent_nums))
print('Highest: ', max(ent_nums))
print('Done')