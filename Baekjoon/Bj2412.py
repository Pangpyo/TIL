# 2412 암벽 등반 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    n, T = map(int, input().split())
    dim = set(tuple(map(int, input().split())) for _ in range(n))
    visit = set()
    que = deque([(0, 0, 0)])
    dist = (-2, -1, 0, 1, 2)
    while que :
        x, y, d = que.popleft()
        for i in dist :
            for j in dist:
                nx = x + i
                ny = y + j
                if (nx, ny) not in dim or (nx, ny) in visit :
                    continue
                if ny == T :
                    return d+1
                visit.add((nx, ny))
                que.append((nx, ny, d+1))
    return -1

if __name__ == "__main__" :
    print(solution())