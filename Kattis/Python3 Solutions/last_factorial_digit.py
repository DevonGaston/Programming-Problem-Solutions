cases = int(input())
for i in range(0, cases):
    n = int(input())
    ans = 1
    for j in range(1, n+1):
        ans *= j
        ans %= 10
    print(ans)
