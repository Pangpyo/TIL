# 1311 할 일 정하기1 G1


def solution():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    inf = float("inf")
    D = [[-1] * (1 << N) for _ in range(N)]

    def dfs(U, visit):
        if U == N:
            return 0
        if D[U][visit] != -1:
            return D[U][visit]
        temp = inf
        for i in range(N):
            if visit & 1 << i:
                continue
            temp = min(temp, P[U][i] + dfs(U + 1, visit | (1 << i)))
        D[U][visit] = temp
        return temp

    return dfs(0, 0)


if __name__ == "__main__":
    print(solution())
