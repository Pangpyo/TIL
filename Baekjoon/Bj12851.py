# 12851 숨바꼭질2 G4

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
q = deque()
q.append((n, cnt))  # 수빈이의 첫 위치와 시간을 저장해두었다
visit = [0] * (max(n, k) * 2 + 3)  # visit의 범위를 넉넉하게 잡아두었다
ans = []
while q:  # BFS를 진행한다
    a, b = q.popleft()  # 위치, 시간을 팝한다.
    visit[a] = 1  # 방문처리
    if a == k:
        ans.append((a, b))  # 방법의 개수를 알아야하므로, ans를 append해준다

    if a > (max(n, k) + 1) or a < 0:  # a가 범위 밖으로 벗어나면 continue해준다
        continue
    na1 = a + 1  # 각 이동 조건 처리
    na2 = a - 1
    na3 = a * 2
    if visit[na1] == 0:  # 방문하지 않은 곳일때만
        q.append((na1, b + 1))  # 큐에 추가해주고, 시간을 +1해준다
    if visit[na2] == 0:
        q.append((na2, b + 1))
    if visit[na3] == 0:
        q.append((na3, b + 1))
minway = ans[0][1]  # 최소시간을 구해준다
mincnt = 0  # 최소시간으로 갈 수 있는 방법의 수
for i in ans:  # 도착하는 방법중 최소시간으로 갈 수 있는 방법의 수를 구해준다
    if i[1] == minway:
        mincnt += 1
print(minway)
print(mincnt)
