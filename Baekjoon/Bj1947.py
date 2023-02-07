# 1947 선물 전달 G3

N = int(input())

D = [0, 0, 1, 2] + [0] * (N - 3)


def div(N):
    return N % 1000000000


for i in range(4, N + 1):
    D[i] = div((i - 1) * (div(D[i - 1]) + div(D[i - 2])))

print(D[N])
