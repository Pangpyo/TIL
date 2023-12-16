# 17394 핑거 스냅 G5


from collections import deque


def solution() :
    p = 100_000
    is_prime = [1]*(p+1)
    for i in range(2, p+1):
        if is_prime[i] :
            for j in range(i*2, p+1, i) :
                is_prime[j] = 0
    T = int(input())
    answers = [0]*T


    def bfs(N, A, B) :
        visit = [-1]*(p*10 + 1)
        que = deque()
        visit[N] = 0
        que.append(N)
        if A <= N <= B and is_prime[N]:
            return 0
        while que :
            n = que.popleft()
            for nn in (n//2, n//3, n+1, n-1) :
                if nn >= p*10 or nn < 0 :
                    continue
                if visit[nn] >= 0:
                    continue
                if A <= nn <= B and is_prime[nn]:
                    return visit[n] + 1
                visit[nn] = visit[n] + 1
                que.append(nn)
        return -1

    for t in range(T) :
        N, A, B = map(int, input().split())
        answers[t] = bfs(N, A, B)
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')