# 2961 도영이가 만든 맛있는 음식 S2

N = int(input())

ing = [tuple(map(int, input().split())) for _ in range(N)]

diffs = []


def bt(n, a, b):
    if n:
        diffs.append(abs(a - b))
    if n == N:
        return
    for i in range(n, N):
        na, nb = ing[i]
        bt(i + 1, a * na, b + nb)


bt(0, 1, 0)


print(min(diffs))
