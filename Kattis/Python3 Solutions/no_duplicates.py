print('yes' if (lambda z: len(z) == len(set(z)))(input().split()) else 'no')
