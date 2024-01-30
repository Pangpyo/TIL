# 1025 제곱수 G5

from math import sqrt


def solution() :
    N, M = map(int, input().split())
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0 ,1)
    nums = tuple(tuple(map(int, list(input()))) for _ in range(N))
    answer = -1
    def dfs(x, y, n, d, a, b) :
        nonlocal answer
        if not (0 <= x < N and 0 <= y < M) :
            return
        n = n*10+nums[x][y]
        if int(sqrt(n))**2 == n :
            answer = max(answer, n)
        nx = x + dx[d]*a
        ny = y + dy[d]*b
        dfs(nx, ny, n, d, a, b)
    
    for i in range(N) :
        for j in range(M) :
            for d in range(8) :
                for a in range(1, N+1) :
                    for b in range(1, M+1) :
                        dfs(i, j, 0, d, a, b)

    return answer

if __name__ == "__main__" :
    print(solution())