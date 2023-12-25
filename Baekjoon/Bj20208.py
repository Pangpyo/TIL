# 20208 진우의 민트초코우유 G5

from itertools import permutations


def solution() :
    N, M, H = map(int, input().split())
    maps = tuple(tuple(map(int, input().split())) for _ in range(N))
    mint = []
    sx, sy = 0, 0
    for i in range(N) :
        for j in range(N) :
            if maps[i][j] == 1 :
                sx, sy = i, j
            elif maps[i][j] == 2 :
                mint.append((i, j))
    answer = 0
    for order in permutations(range(len(mint))) :
        x, y = sx, sy
        m = M
        cnt = 0
        for i in order :
            nx, ny = mint[i]
            m -= abs(nx-x) + abs(ny-y)
            if m < 0 :
                break
            cnt += 1
            m += H
            if abs(nx-sx) + abs(ny-sy) <= m :
                answer = max(cnt, answer)
            x, y = nx, ny
    return answer

if __name__ == "__main__" :
    print(solution())