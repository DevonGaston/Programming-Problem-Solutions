line = input()
while line is not None:
    a, b = map(int, line.split())
    print(abs(a-b))
    try:
        line = input()
    except:
        break
