# 12852 1로만들기 2

from collections import deque


N = int(input())

que = deque([([N])])
visit = []
while que:
    n = que.popleft()
    if n[-1] == 1:
        print(len(n) - 1)
        print(*n)
        break
    n1 = n[-1] // 3 if n[-1] % 3 == 0 else False
    n2 = n[-1] // 2 if n[-1] % 2 == 0 else False
    n3 = n[-1] - 1
    if n1 and n1 not in visit:
        visit.append(n1)
        que.append((n + [n1]))
    if n2 and n2 not in visit:
        visit.append(n2)
        que.append((n + [n2]))
    if n3 not in visit:
        visit.append(n3)
        que.append((n + [n3]))
