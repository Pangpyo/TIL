# 18428 감시 피하기 G5

def solution() :
    N = int(input())
    room = [list(input().split()) for _ in range(N)]
    T = []
    for i in range(N) :
        for j in range(N) :
            if room[i][j] == 'T' :
                T.append((i, j))
    x = "X"
    o = "O"
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def check() :
        for x, y in T :
            for i in range(4) :
                nx = x
                ny = y
                while 0 <= nx < N and 0 <= ny < N :
                    if room[nx][ny] == 'S' :
                        return False
                    elif room[nx][ny] == "O" :
                        break
                    nx += dx[i]
                    ny += dy[i]
        return True

    for i in range(N*N) :
        if room[i//N][i%N] != x :
            continue
        room[i//N][i%N] = o
        for j in range(i+1, N*N) :
            if room[j//N][j%N] != x :
                continue
            room[j//N][j%N] = o
            for k in range(j+1, N*N) :
                if room[k//N][k%N] != x :
                    continue
                room[k//N][k%N] = o
                if check() :
                    return "YES"
                room[k//N][k%N] = x
            room[j//N][j%N] = x
        room[i//N][i%N] = x

    return "NO"

if __name__ == "__main__" :
    print(solution())