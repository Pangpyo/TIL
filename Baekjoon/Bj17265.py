# 17265 나의 인생에는 수학과 함께 G5

def solution() :
    N = int(input())
    P = tuple(tuple(input().split()) for _ in range(N))
    INF = 1<<20
    answer = [-INF, INF]
    dx = (0, 1)
    dy = (1, 0)
    temp = [P[0][0]]*(N*2-1)

    def dfs(x, y, d) :
        if d == N*2-2 :
            res = int(temp[0])
            for i in range(2, N*2, 2) :
                res = eval(str(res)+temp[i-1]+temp[i])
            answer[0] = max(res, answer[0])
            answer[1] = min(res, answer[1])
            return
        for i in range(2) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N :
                continue
            temp[d+1] = P[nx][ny]
            dfs(nx, ny, d+1)
    
    dfs(0, 0 ,0)

    return answer

if __name__ == "__main__" :
    print(*solution())