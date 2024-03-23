# 12190 Minesweeper (Small) G5

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    T = int(input())
    answers = []
    for t in range(1, T+1) :
        N = int(input())
        maps = list(list(input().rstrip()) for _ in range(N))
        dx = (-1, -1, -1, 0, 0, 1, 1, 1)
        dy = (-1, 0, 1, -1, 1, -1, 0, 1)
        visit = [[0]*N for _ in range(N)]
        for i in range(N) :
            for j in range(N) :
                if maps[i][j] == '*' :
                    for d in range(8) :
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N :
                            continue
                        if maps[nx][ny] == '*' :
                            continue
                        maps[nx][ny] = '-'
        
        def dfs(x, y) :
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N :
                    continue
                if maps[nx][ny] == '*' :
                    continue
                if visit[nx][ny] :
                    continue
                visit[nx][ny] = 1
                if maps[nx][ny] == "." :
                    dfs(nx, ny)
        answer = 0
        for i in range(N) :
            for j in range(N) :
                if maps[i][j] == '.' and not visit[i][j]:
                    visit[i][j] = 1
                    dfs(i, j)
                    answer += 1
        for i in range(N) :
            for j in range(N) :
                if not visit[i][j] and maps[i][j] != '*' :
                    answer += 1
        answers.append(f"Case #{t}: {answer}")
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')