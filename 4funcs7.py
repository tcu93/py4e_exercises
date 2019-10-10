def calc_score(score):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    else:
        print('C')


score = float(input('Enter score: \n'))

calc_score(score)

