# 14867 물통 G2
from collections import deque


a, b, c, d = map(int, input().split())

visit = set()


def move_water(x, y, desti):
    diff = desti - y
    if x >= diff:
        return x - diff, desti
    else:
        return 0, y + x


que = deque([(0, 0, 0)])
ans = -1
if c == d == 0:
    ans = 0
else:
    while que:
        x, y, cnt = que.popleft()
        if (a, y) not in visit:
            if a == c and y == d:
                ans = cnt + 1
                break
            visit.add((a, y))
            que.append((a, y, cnt + 1))
        if (x, b) not in visit:
            if x == c and b == d:
                ans = cnt + 1
                break
            visit.add((x, b))
            que.append((x, b, cnt + 1))
        if (0, y) not in visit:
            if 0 == c and y == d:
                ans = cnt + 1
                break
            visit.add((0, y))
            que.append((0, y, cnt + 1))
        if (x, 0) not in visit:
            if x == c and 0 == d:
                ans = cnt + 1
                break
            visit.add((x, 0))
            que.append((x, 0, cnt + 1))
        mx1, my1 = move_water(x, y, b)
        if (mx1, my1) not in visit:
            if mx1 == c and my1 == d:
                ans = cnt + 1
                break
            visit.add((mx1, my1))
            que.append((mx1, my1, cnt + 1))
        my2, mx2 = move_water(y, x, a)
        if (mx2, my2) not in visit:
            if mx2 == c and my2 == d:
                ans = cnt + 1
                break
            visit.add((mx2, my2))
            que.append((mx2, my2, cnt + 1))
print(ans)
