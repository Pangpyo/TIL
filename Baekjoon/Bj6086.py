# 6086 최대 유량 G4

from collections import defaultdict, deque
import sys


input = sys.stdin.readline

n = int(input())

P = defaultdict(dict)  # 해당 파이프에서 다른 파이로 가는 최대 유량 저장
L = defaultdict(set)  # 해당 파이프에서 경로들
F = defaultdict(dict)  # 현재 흐르는 유량
for _ in range(n):
    u, v, n = input().split()
    F[u][v] = 0
    F[v][u] = 0
    if v in P[u]:
        P[u][v] += int(n)
    else:
        P[u][v] = int(n)
    if u in P[v]:
        P[v][u] += int(n)
    else:
        P[v][u] = int(n)
    L[u].add(v)
    L[v].add(u)


que = deque(["A"])


def makeflow(prev):  # 방문한 노드들을 따라서
    flow = 1001  # 맥시멈 값
    cur = "Z"  # 끝부터 돌아옴
    while cur != "A":  # 시작지점까지 역순으로 돌아감
        flow = min(flow, P[prev[cur]][cur] - F[prev[cur]][cur])  # 최소유량을 구한다
        cur = prev[cur]  # 하나씩 역순으로
    cur = "Z"
    while cur != "A":  # 지나온 자리들에 최소유량을 더해주고, 역순에는 음수로 유량을 더해준다
        F[prev[cur]][cur] += flow
        F[cur][prev[cur]] -= flow
        cur = prev[cur]
    return flow  # 구한 유량을 더해준다


def bfs():
    prev = {}  # 이전의 노드 저장
    que = deque(["A"])  # bfs진행
    while que:
        cur = que.popleft()
        for ncur in L[cur]:
            if (
                P[cur][ncur] > F[cur][ncur] and ncur not in prev
            ):  # 흐를 수 있는 유량이 남았고, 이전에 방문한노드가 아닌 경우
                prev[ncur] = cur  # 이전 노드 저장
                que.append(ncur)  # bfs추가
                if ncur == "Z":  # 목표까지 가는 경로가 있는 경우
                    return makeflow(prev)  # flow를 만든다
    return -1


ans = 0
while 1:
    flow = bfs()
    if flow > 0:
        ans += flow
    else:
        break
print(ans)
