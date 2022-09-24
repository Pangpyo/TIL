
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
        global ans
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= len(miro) or nx < 0 or ny >= len(miro[0]) or ny < 0 :
            continue
        if len(ways) == k :
            return
        if ans :
            return
        if len(ways) == (k-1) and miro[nx][ny] == 1:
            ans = ''.join([ways,wayname(i)])
            print(''.join([ways,wayname(i)]))
            return
        else :    
            dfs(nx, ny, ''.join([ways,wayname(i)]), miro, k)
dx = [1, 0, 0, 1]
dy = [0, -1, 1, 0]
ans = 0

def solution(n, m, x, y, r, c, k):
    miro = [[0]*m for _ in range(n)]
    miro[r-1][c-1] = 1

    dfs(x-1, y-1, '', miro, k)
    global ans
    if not ans :
        ans = 'impossible'
    return ans
