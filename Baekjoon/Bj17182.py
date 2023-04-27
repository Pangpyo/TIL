# 17182 우주 탐사선 G3


def solution():
    N, K = map(int, input().split())
    dist = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = float("inf")

    def dfs(pre, cnt, d):
        nonlocal ans
        if cnt == N:
            ans = min(ans, d)
            return
        for i in range(N):
            if visit[i]:
                continue
            visit[i] = 1
            dfs(i, cnt + 1, d + dist[pre][i])
            visit[i] = 0

    visit = [0] * N
    visit[K] = 1

    dfs(K, 1, 0)

    return ans


if __name__ == "__main__":
    print(solution())
