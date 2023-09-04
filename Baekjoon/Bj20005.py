# 20005 보스몬스터 전리품 G3

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, M, P = map(int, input().split())
    maps = []
    players = {}
    for i in range(N) :
        temp = list(input().rstrip())
        for j in range(M) :
            if temp[j] == 'B' :
                bx, by = i, j
        maps.append(temp)

    for _ in range(P) :
        p, dps = input().split()
        players[p] = int(dps)
    boss = int(input())
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    que = deque()
    que.append((bx, by))
    visit = [[0]*M for _ in range(N)]
    ans = 0
    time = 0
    totalDps = 0
    while que :
        boss -= totalDps
        if boss <= 0 :
            break
        for _ in range(len(que)) :
            x, y = que.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0 :
                    continue
                if visit[nx][ny] or maps[nx][ny] == 'X' :
                    continue
                visit[nx][ny] = visit[x][y] + 1
                if maps[nx][ny].islower() :
                    totalDps += players[maps[nx][ny]]
                    ans += 1
                que.append((nx, ny))
    
    return ans

if __name__ == "__main__" :
    print(solution())