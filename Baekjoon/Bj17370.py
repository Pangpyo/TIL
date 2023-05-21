# 17370 육각형 우리 속의 개미 G3

def solution() :
    P = [[0]*50 for _ in range(50)]
    N = int(input())
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ans = 0
    def dfs(x, y, px, py, cnt) :
        nonlocal ans
        if P[x][y] :
            if cnt == N :
                ans += 1
            return
        if cnt == N :
            return
        P[x][y] = 1
        for i in range(4) :
            if i == 0 and (x+y)%2 :
                continue
            if i == 2 and not (x+y)%2 :
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == px and ny == py :
                continue
            dfs(nx, ny, x, y, cnt+1)
        P[x][y] = 0
    P[25][25] = 1
    dfs(24, 25, 25, 25, 0)
    return ans

if __name__ == "__main__" :
    print(solution())