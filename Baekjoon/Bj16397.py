# 16397 탈출 G4

from collections import deque

N, T, G = map(int, input().split())

que = deque()

que.append((N, 0))

visit = set()
visit.add(N)


def make_B(n):
    if 0 < n * 2 <= 99999:
        nn = n * 2
        k = 1
        while nn >= 10:
            nn //= 10
            k *= 10
        return n * 2 - k
    else:
        return 0


def bfs():
    if N == G:
        return 0
    while que:
        n, d = que.popleft()
        if d == T:
            return "ANG"
        if n < 99999 and n + 1 not in visit:
            if n + 1 == G:
                return d + 1
            que.append((n + 1, d + 1))
            visit.add(n + 1)
        B = make_B(n)
        if B and B not in visit:
            if B == G:
                return d + 1
            que.append((B, d + 1))
            visit.add(B)
    return "ANG"


print(bfs())
