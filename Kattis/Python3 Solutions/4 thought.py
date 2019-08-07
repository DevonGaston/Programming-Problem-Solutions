ops = [' + ', ' - ', ' * ', ' // ']
val = {}
for a in ops:
    for b in ops:
        for c in ops:
            v_str = "4{:s}4{:s}4{:s}4".format(a,b,c)
            v = eval(v_str)
            val[v] = v_str.replace('//', '/') + " = {:d}".format(v)

for i in range(0, int(input())):
    n = int(input())
    if n < -60 or n > 256 or n not in val:
        print("no solution")
    else:
        print(val[n])
