# 20924 트리의 기둥과 가지 G4
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, R = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        u, v, d = map(int, input().split())
        tree[u].append((v, d))
        tree[v].append((u, d))
    answer = [0, 0]
    visit = [0]*(N+1)
    def dfs(n, l, ispillar) :
        visit[n] = 1
        if ispillar :
            isstart = 1 if n == R else 0
            if len(tree[n]) >= 3-isstart or len(tree[n]) + isstart == 1 :
                ispillar = False
                answer[0] = l
                l = 0
        else :
            answer[1] = max(l, answer[1])
        for nn, d in tree[n] :
            if not visit[nn] :
                dfs(nn, l+d, ispillar)
    dfs(R, 0, True)

    return answer

if __name__ == "__main__" :
    print(*solution())