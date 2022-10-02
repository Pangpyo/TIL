# 16953 A → B S2

from collections import deque


A, B = map(int, input().split())
que = deque([(A, 1)])
ans = -1
while que:
    n, cnt = que.popleft()
    if n == B:
        ans = cnt
        break
    if n > B:
        continue
    n1 = n * 2
    n2 = n * 10 + 1
    que.append((n1, cnt + 1))
    que.append((n2, cnt + 1))

print(ans)
