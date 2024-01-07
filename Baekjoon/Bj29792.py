# 29792 규칙적인 보스돌이 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    C = [int(input()) for _ in range(N)]
    C.sort(reverse=True)
    boss = [tuple(map(int, input().split())) for _ in range(K)]
    TIME = 60*15
    def dfs(t, m, n) :
        temp = m
        for i in range(n, K) :
            if C[c]*t - boss[i][0] >= 0 :
                use = boss[i][0] // C[c]
                if boss[i][0] % C[c] :
                    use += 1
                
                temp = max(temp, dfs(t-use, m+boss[i][1], i+1))
        m = temp
        return m
    answer = 0
    for c in range(M) :
        answer += dfs(TIME, 0, 0)

    return answer

if __name__ == "__main__" :
    print(solution())