# 12851 숨바꼭질2 G4

import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())

cnt = 0
q = deque()
q.append((n,cnt))
visit = [0]*(max(n, k)*2+3)
ans = []
while q:
    a,b = q.popleft()
    visit[a] = 1
    if a == k:
        ans.append((a, b))
        
    if a > (max(n, k)+1) or a < 0 :
        continue
    na1 = a + 1
    na2 = a - 1
    na3 = a * 2
    if visit[na1] == 0 :
        q.append((na1,b+1))
    if visit[na2] == 0 :
        q.append((na2,b+1))
    if visit[na3] == 0 :
        q.append((na3,b+1))
minway = ans[0][1]
mincnt = 0
for i in ans :
    if i[1] == minway :
        mincnt += 1
print(minway)
print(mincnt)