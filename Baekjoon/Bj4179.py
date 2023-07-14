# 4179 불! G4

from collections import deque
import sys



def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    room = []
    J = []
    fire = []
    for i in range(N) :
        temp = list(input())
        for j in range(M) :
            if temp[j] == "J" :
                J.append((i, j))
            elif temp[j] == "F" :
                fire.append((i, j))
        room.append(temp)
    inf = sys.maxsize
    visit = [[inf]*M for _ in range(N)]
    
    def bfs(points, man) :
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        que = deque()
        for x, y in points :
            que.append((x, y))
            visit[x][y] = 0
        while que :
            x, y = que.popleft()
            cnt = visit[x][y]
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0 :
                    if man :
                        return cnt + 1
                    continue
                if visit[nx][ny] <= cnt + 1 or room[nx][ny] == "#":
                    continue
                visit[nx][ny] = cnt + 1
                que.append((nx, ny))
        return "IMPOSSIBLE"
    bfs(fire, False)
    ans = bfs(J, True)

    return ans

if __name__ == "__main__" :
    print(solution())  