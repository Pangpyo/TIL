# 21772 가희와 고구마 먹방 G5

import sys


def solution() :
    input = sys.stdin.readline
    R, C, T = map(int, input().split())
    maps = []
    sx, sy = 0, 0
    for i in range(R) :
        temp = input().rstrip()
        for j in range(C): 
            if temp[j] == 'G' :
                sx, sy = i, j
        maps.append(list(temp))
    dx = (-1 ,0, 1 ,0)
    dy = (0, 1, 0, -1)
    answer = 0
    def dfs(x, y, d, a) :
        nonlocal answer
        if d == T :
            answer = max(answer, a)
            return
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            flag = False
            if nx >= R or nx < 0 or ny >= C or ny < 0 :
                continue
            if maps[nx][ny] == '#':
                continue
            elif maps[nx][ny] == 'S' :
                flag = True
                maps[nx][ny] = '.'
            dfs(nx, ny, d+1, a+int(flag))
            if flag :
                maps[nx][ny] = 'S'
    
    dfs(sx, sy, 0, 0)

    return answer

if __name__ == "__main__" :
    print(solution())