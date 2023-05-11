# 17069 파이프 옮기기2 G4


def solution():
    N = int(input())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))
    visit = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
    visit[-1][-1] = [1, 1, 1]

    def dfs(x, y, d):
        if visit[x][y][d] != -1:
            return visit[x][y][d]
        temp = 0
        if d != 0 and x + 1 < N and not board[x + 1][y]:
            temp += dfs(x + 1, y, 2)
        if d != 2 and y + 1 < N and not board[x][y + 1]:
            temp += dfs(x, y + 1, 0)
        if (
            x + 1 < N
            and y + 1 < N
            and not board[x + 1][y]
            and not board[x][y + 1]
            and not board[x + 1][y + 1]
        ):
            temp += dfs(x + 1, y + 1, 1)
        visit[x][y][d] = temp
        return visit[x][y][d]

    ans = dfs(0, 1, 0)
    return ans


if __name__ == "__main__":
    print(solution())
