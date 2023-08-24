# 14945 불장난 G4

def solution() :
    N = int(input())
    D = [[[0]*N for _ in range(N)] for _ in range(N)]
    D[0][0][0] = 1
    dx = (0, 0, 1, 1)
    dy = (0, 1, 0, 1)
    mod = 10007
    for i in range(N-1) :
        for x in range(i+1) :
            for y in range(i+1) :
                if not D[i][x][y] :
                    continue
                for d in range(4) :
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx == ny :
                        continue
                    D[i+1][nx][ny] += D[i][x][y] 
            D[i][x][y] %= mod
    return sum(map(sum, D[-1])) % mod

if __name__ == "__main__" :
    print(solution())