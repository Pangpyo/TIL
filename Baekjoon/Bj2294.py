# 2294 동전2 G5

n, k = map(int, input().split())

coins = []
D = [-1] * (k + 1)
D[0] = 0
for i in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.append(coin)
    D[coin] = 1

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0 and D[i - coin] >= 0:
            if D[i] < 0:
                D[i] = D[i - coin] + 1
            else:
                D[i] = min(D[i - coin] + 1, D[i])

print(D[-1])
