dominant = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
nondominant = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
n, b = input().split()
val = 0
for i in range(int(n)*4):
    card = input()
    if card[1] == b:
        val += dominant[card[0]]
    else:
        val += nondominant[card[0]]
print(val)
    
