# 27971 강아지는 많을수록 좋다 S1

from collections import deque


def solution():
    N, M, A, B = map(int, input().split())
    blocked = [0]*(N+1)
    for _ in range(M):
        l, r = map(int, input().split())
        for i in range(l, r+1):
            blocked[i] = 1
    que = deque()
    que.append(0)
    visit = [-1]*(N+1)
    visit[0] = 0
    while que:
        n = que.popleft()
        v = visit[n]
        for d in (A, B):
            nn = n + d
            if nn > N:
                continue
            if visit[nn] != -1 or blocked[nn]:
                continue
            que.append(nn)
            visit[nn] = v + 1
            if nn == N:
                return visit[nn]
    return visit[-1]

if __name__ == "__main__":
    print(solution())