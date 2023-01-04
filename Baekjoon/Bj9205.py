# 9205 맥주 마시면서 걸어가기 G5

from collections import deque
import sys


input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    que = deque()
    que.append(tuple(map(int, input().split())))

    store = [tuple(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    ex, ey = tuple(map(int, input().split()))

    def answer():
        while que:
            x, y = que.popleft()
            if abs(ex - x) + abs(ey - y) <= 1000:
                return "happy"
            for i in range(n):
                if visit[i]:
                    continue
                nx, ny = store[i]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    que.append((nx, ny))
                    visit[i] = 1
        return "sad"

    print(answer())
