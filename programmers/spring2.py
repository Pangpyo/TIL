def solution(grid):
    ngrid = []
    for g in grid:
        ngrid.append(list(g))
    n = len(ngrid)
    m = len(ngrid[0])
    visit = [[0] * m for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        stack = [(x, y)]
        dots = [(x, y)]
        flag = True
        visit[x][y] = 1
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= n or nx < 0 or ny >= m or ny < 0:
                    flag = False
                    continue
                if visit[nx][ny]:
                    continue
                if ngrid[nx][ny] == ".":
                    stack.append((nx, ny))
                    dots.append((nx, ny))
                    visit[nx][ny] = 1
        if flag:
            for x, y in dots:
                ngrid[x][y] = "#"

    for i in range(n):
        for j in range(m):
            if not visit[i][j] and ngrid[i][j] == ".":
                dfs(i, j)
    answer = 0
    for i in range(n):
        answer += ngrid[i].count("#")
    return answer


grid = [
    ".....####",
    "..#...###",
    ".#.##..##",
    "..#..#...",
    "..#...#..",
    "...###...",
]


print(solution(grid))
