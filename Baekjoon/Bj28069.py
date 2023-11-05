# 28069 김밥천국의 계단 G5

from collections import deque


def solution() :
    N, K = map(int, input().split())
    visit = [-1]*(N+1)
    visit[0] = 0
    que = deque()
    que.append(0)
    while que :
        n = que.popleft()
        if visit[n] > K :
            break
        for nn in (n+1, n+n//2) :
            if nn > N :
                continue
            if visit[nn] != -1 :
                continue
            visit[nn] = visit[n] + 1
            que.append(nn)

    answer = 'water'
    if visit[N] != -1 and visit[N] <= K :
        answer = 'minigimbob'
    return answer

if __name__ == "__main__" :
    print(solution())