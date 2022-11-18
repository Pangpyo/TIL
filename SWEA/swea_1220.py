# swea 1220 D3
import sys


sys.stdin = open("input.txt")

for t in range(1, 11):
    N = int(input())
    cnt = 0
    table = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        go = False
        for j in range(N):
            if table[j][i] == 1 and not go:
                go = True
            elif table[j][i] == 2 and go:
                go = False
                cnt += 1
    print(f"#{t} {cnt}")
