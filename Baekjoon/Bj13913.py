# 13913 숨바꼭질 4 G4

from collections import deque


def solution() :
    N, K = map(int, input().split())
    M = 100001
    visit = [-1]*M
    visit[N] = -2
    que = deque()
    que.append(N)
    while que :
        n = que.popleft()
        for nn in (n-1, n+1, n*2) :
            if nn >= M or nn < 0 :
                continue
            if visit[nn] != -1 :
                continue
            visit[nn] = n
            que.append(nn)
    ans = []
    now = K
    while True :
        if now == -2 :
            break
        ans.append(now)
        now = visit[now]
    ans.reverse()
    print(len(ans)-1)
    return ans

if __name__ == "__main__" :
    print(*solution())