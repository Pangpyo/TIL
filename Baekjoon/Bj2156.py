# 2156 포도주 시식 S1

n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))
if n == 1:
    print(wine[0])
else:
    D = [(0, wine[0]), (wine[1], wine[0] + wine[1])]

    for i in range(2, n):
        one = max(max(D[i - 2]) + wine[i], D[i - 1][1])
        two = max(D[i - 1][0], D[i - 2][1]) + wine[i]
        D.append((one, two))

    print(max(D[-1]))
