r = list(map(float, input().split()))
while(len(r) == 5):
    print(((abs((r[0]-r[2])**r[4])) + (abs((r[1]-r[3])**r[4])))**(1/r[4]))
    r = list(map(float, input().split()))
