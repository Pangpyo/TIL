# 23085 판치기 G4

from collections import deque


def solution() :
    N, M = map(int, input().split())
    f = 0
    e = 0
    for c in input() :
        if c == "H" :
            f += 1
        else :
            e += 1
    if e == N :
        return 0
    visit = [[0]*(N+1) for _ in range(N+1)]
    que = deque([(f, e, 0)])
    visit[f][e] = 1
    while que :
        f, e, d = que.popleft()
        for i in range(M) :
            nf = f - (M-i)
            ne = e - i
            if nf < 0 or ne < 0 :
                continue
            nf += i
            ne += (M-i)
            if nf < 0 or ne < 0 :
                continue
            if visit[nf][ne] :
                continue
            if ne == N :
                return d+1
            visit[nf][ne] = 1
            que.append((nf, ne, d+1))
            
    return -1

if __name__ == "__main__" :
    print(solution())