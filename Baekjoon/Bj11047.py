# 11047 동전0 S4

N, K = map(int, input().split())
coins = []
for _ in range(N) :
    coins.append(int(input()))
coins = sorted(coins, reverse=True)
ans = 0
for coin in coins :
    ans += K//coin
    K = K%coin
print(ans)