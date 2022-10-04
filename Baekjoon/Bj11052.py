# 11052 카드 구매하기 S1

N = int(input())
cards = list(map(int, input().split()))
D = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1):
        D[j] = max(D[j], D[j - i] + cards[i - 1])
print(D[N])
