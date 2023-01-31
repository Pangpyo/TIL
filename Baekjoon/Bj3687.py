# 3687 성냥개비 G2
import sys


input = sys.stdin.readline
INF = sys.maxsize
mnums = [INF, INF, 1, 7, 4, 2, 0, 8]
mDP = [INF, INF, 1, 7, 4, 2, 6, 8] + [INF] * 93
for i in range(8, 101):
    for j in range(2, 8):
        mDP[i] = min(mDP[i], int(str(mDP[i - j]) + str(mnums[j])))

for _ in range(int(input())):
    N = int(input())
    M = N % 2 * "7" + "1" * ((N // 2) - 1 if N % 2 else N // 2)
    print(mDP[N], M)
