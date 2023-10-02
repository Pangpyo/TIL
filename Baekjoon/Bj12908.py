# 12908 텔레포트 3 G5

def solution() :
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    tel = [list(map(int, input().split())) for _ in range(3)]
    ans = float('inf')
    def dfs(x, y, t, v) :
        nonlocal ans
        if (x, y) == (ex, ey) :
            ans = min(t, ans)
            return
        dfs(ex, ey, abs(x-ex)+abs(y-ey)+t, v)
        for i in range(3) :
            if v & (1<<i) :
                continue
            x1, y1, x2, y2 = tel[i]
            nv = v | (1<<i)
            dfs(x1, y1, t+abs(x2-x)+abs(y2-y)+10, nv)
            dfs(x2, y2, t+abs(x1-x)+abs(y1-y)+10, nv)
    dfs(sx, sy, 0, 0)
    return ans

if __name__ == "__main__" :
    print(solution())