# 16985 Maaaaaaaaaze G2

from collections import deque


def solution() :
    cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

    def rotate(n) :
        ncube = [[0]*5 for _ in range(5)]
        for i in range(5) :
            for j in range(5) :
                ncube[j][-i-1] = cube[n][i][j]
        cube[n] = ncube

    def bfs(x, y) :
        dx = [0, 0, -1, 1, 0, 0]
        dy = [0, 0, 0, 0, -1, 1]
        dz = [-1, 1, 0, 0, 0, 0]
        que = deque([(x, y, 0)])
        ex = 0 if x else 4
        ey = 0 if y else 4
        ez = 4
        visit = [[[0]*5 for _ in range(5)] for _ in range(5)]
        visit[0][x][y] = 1
        inf = 1000
        if not cube[0][x][y] :
            return inf
        while que :
            x, y, z = que.popleft()
            d = visit[z][x][y]
            for i in range(6) :
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx >= 5 or nx < 0 or ny >= 5 or ny < 0 or nz >= 5 or nz < 0 :
                    continue
                if not cube[nz][nx][ny] or visit[nz][nx][ny] :
                    continue
                if (nx, ny, nz) == (ex, ey, ez) :
                    return d
                que.append((nx, ny, nz))
                visit[nz][nx][ny] = d + 1
        return inf
    cnt = 0
    def permu(n) :
        nonlocal ans, cnt
        if n == 5 :
            cnt += 1
            print(*cube, sep="\n")
            print()
            ans = min(bfs(0, 0),
            bfs(0, 4),
            bfs(4, 0),
            bfs(4, 4))
            return
        permu(n+1)
        for _ in range(3) :
            rotate(n)
            permu(n+1)
        rotate(n)
    ans = 1000
    permu(1)
    return ans if ans != 1000 else -1

if __name__ == "__main__" :
    print(solution())