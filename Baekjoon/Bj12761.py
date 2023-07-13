# 12761 돌다리 S1

from collections import deque


def solution() :
    A, B, N, M = map(int, input().split())
    ans = 0
    que = deque()
    visit = [0]*100001
    if N == M :
        return ans
    que.append(N)
    while que :
        n = que.popleft()
        for nn in [n-1, n+1, n*A, n*B, n+A, n+B, n-A, n-B] :
            if nn < 0 or nn > 100000 :
                continue
            if visit[nn] :
                continue
            visit[nn] = visit[n] + 1
            if nn == M :
                return visit[nn]
            que.append(nn)
    return ans

if __name__ == "__main__" :
    print(solution())