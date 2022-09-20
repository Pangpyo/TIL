# 1389 케빈 베이컨의 6단계 법칙

from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfsbacon(n) :
    bacon = [0]*(N+1)
    bacon[n] = -1
    que = deque()
    que.append((graph[n], 0))

    while que :
        temp , d= que.popleft()

        for t in temp :
            if bacon[t] == 0 :
                bacon[t] = d + 1
                que.append((graph[t], bacon[t]))
    return sum(bacon)+1
ans = []
for i in range(1, N+1) :
    ans.append((bfsbacon(i), i))
ans.sort()
print(ans[0][1])
