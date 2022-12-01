# 1057 토너먼트 S3

N, K, M = map(int, input().split())
i = 0


def div(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n + 1) // 2


while K != M:
    K = div(K)
    M = div(M)
    i += 1
print(i)
