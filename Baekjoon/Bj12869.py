# 12869 뮤탈리스크 G4

from collections import deque
from itertools import permutations


n = int(input())

que = deque([(tuple(map(int, input().split())), 0)])
C = list(permutations(list(range(n)), n))


def answer():
    visit = {}
    while que:
        scv, cnt = que.popleft()
        for c in C:
            nscv = tuple(
                scv[c[i]] - 9 // 3 ** i if scv[c[i]] - 9 // 3**i > 0 else 0
                for i in range(n)
            )
            if max(nscv) <= 0:
                return cnt + 1
            if nscv in visit:
                continue
            visit[nscv] = 1
            que.append((nscv, cnt + 1))


print(answer())
