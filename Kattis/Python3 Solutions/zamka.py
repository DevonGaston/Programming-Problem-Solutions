l = int(input())
d = int(input())
x = int(input())
def sum_dig(i):
    t = 0
    while i > 0:
        t +=i%10
        i //= 10
    return t
v = [i for i in range (l, d+1) if sum_dig(i) == x]
print(v[0])
print(v[-1])
