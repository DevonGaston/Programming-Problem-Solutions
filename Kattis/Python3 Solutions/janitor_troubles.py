from math import sqrt
a, b, c, d = list(map(float, input().split()))
semiperimeter = (a + b + c + d)/2
print(sqrt((semiperimeter - a) * (semiperimeter - b) * ( semiperimeter - c)
           * (semiperimeter - d)))
