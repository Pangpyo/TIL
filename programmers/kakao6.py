from collections import deque
from tkinter import N

def wayname(n) :
    if n == 0 :
        return 'd'
    elif n == 1 :
        return 'l'
    elif n == 2 :
        return 'r'
    else :
        return 'u'

def dfs(x, y, ways, miro, k) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= len(miro) or nx < 0 or ny >= len(miro[0]) or ny < 0 :
            continue
        if len(ways) == k :
            break
        if len(ways) == (k-1) and miro[nx][ny] == 1:
            return ''.join([ways,wayname(i)])
        else :    
            dfs(nx, ny, ''.join([ways,wayname(i)]), miro, k)
dx = [1, 0, 0, 1]
dy = [0, -1, 1, 0]


def solution(n, m, x, y, r, c, k):
    miro = [[0]*m for _ in range(n)]
    miro[r-1][c-1] = 1

    ans = dfs(x-1, y-1, '', miro, k)
    
    # while 1 :
    #     x, y, ways = que.popleft()
    #     if len(ways) == k :
    #         break
    #     for i in range(4) :
    #         nx = x+dx[i]
    #         ny = y+dy[i]
    #         if nx >= n or nx < 0 or ny >= m or ny < 0 :
    #             continue
    #         if len(ways) == (k-1) and miro[nx][ny] == 1:
    #             ans.append(ways+wayname(i))
    #         else :    
    #             que.append((nx, ny, ''.join([ways,wayname(i)])))
    if ans :
        ans.sort()
        answer = ans[0]
    else :
        answer = 'impossible'
    return ans


# dlru 아래 왼 오 위