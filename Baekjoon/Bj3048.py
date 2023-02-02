# 3048 개미 S4

N1, N2 = map(int, input().split())

A1 = input()[::-1]
A2 = input()

T = int(input())

move = [0] * (N1 + N2)

idxs = list(range(N1)) + [N1 + N2]


for i in range(T):
    for j in range(N1):
        if j + 1 < N1 + N2:
            if idxs[j] + 1 < idxs[j + 1]:
                idxs[j] += 1

for i in range(N1):
    move[idxs[i]] = A1[i]

idx2 = 0
for i in range(N1 + N2):
    if not move[i]:
        move[i] = A2[idx2]
        idx2 += 1
print(*move, sep="")
