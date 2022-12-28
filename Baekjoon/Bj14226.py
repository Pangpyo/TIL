# 14226 이모티콘 G4

from collections import deque


S = int(input())


def bfs():
    que = deque([(1, 0, 0)])
    visit = set()
    visit.add((1, 0))
    while que:
        R, C, t = que.popleft()
        if R + C == S or R == S or R - 1 == S:
            return t + 1
        if C and (R + C, C) not in visit:
            que.append((R + C, C, t + 1))
            visit.add((R + C, C))
        if (R, R) not in visit:
            que.append((R, R, t + 1))
            visit.add((R, R))
        if R > 1 and (R - 1, C) not in visit:
            que.append((R - 1, C, t + 1))
            visit.add((R - 1, C))


print(bfs())
