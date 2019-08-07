num = list(map(int, input().split()))
order = input()
ans = []
num.sort()
dic = {"A":num[0], "B":num[1], "C":num[2]}
for i in order:
    ans.append(str(dic.get(i)))
print(ans[0] + " " + ans[1] + " " + ans[2])
