# 10472 십자뒤집기 G5

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    bits = [0]*9
    dx = (0, -1, 0, 1, 0)
    dy = (0, 0, 1, 0, -1)
    for x in range(3):
        for y in range(3):
            for d in range(5):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 3 or nx < 0 or ny >= 3 or ny < 0:
                    continue
                bits[x*3+y] += 1<<(nx*3+ny)
    for t in range(T):
        target = 0
        for i in range(3):
            for j, m in enumerate(input().rstrip()):
                if m == '*':
                    target += 1<<(i*3+j)
        if target == 0:
            continue
        def bfs(target):
            que = deque()
            que.append(0)
            visit = [-1]*(1<<10)
            visit[0] = 0
            while que:
                bit = que.popleft()
                d = visit[bit]
                for i in range(9):
                    nbit = bit^bits[i]
                    if nbit == target:
                        return d+1
                    if visit[nbit] == -1:
                        que.append(nbit)
                        visit[nbit] = d+1
            return 0
        answer[t] = bfs(target)
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')