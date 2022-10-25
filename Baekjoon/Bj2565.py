# 2565 전깃줄 G5

N = int(input())

lines = []

for i in range(N):
    lines.append(tuple(map(int, input().split())))

lines = [j for i, j in sorted(lines)]


def longest(list, N):
    D = [1] * (N)
    for i in range(1, N):
        for j in range(i):
            if list[i] > list[j]:
                D[i] = max(D[i], D[j] + 1)
    return max(D)


maxinc = longest(lines, N)


print(N - maxinc)
