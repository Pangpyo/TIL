# 21608 상어 초등학교 G5

import sys


def solution() :
    input = sys.stdin.readline 
    N = int(input())
    dx = (-1, 0, 1 ,0)
    dy = (0, 1, 0, -1)
    D = [[0]*N for _ in range(N)]
    score = [0, 1, 10, 100, 1000]
    likes = [[] for _ in range(N*N+1)]
    ans = 0
    for k in range(N*N) :
        nums = list(map(int, input().split()))
        likes[nums[0]] = nums[1::]
        el, ee, ex, ey = -1, -1, 0, 0
        for x in range(N) :
            for y in range(N) :
                if D[x][y] :
                    continue
                l = 0
                e = 0
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= N or nx < 0 or ny >= N or ny < 0 :
                        continue
                    if D[nx][ny] in nums :
                        l += 1
                    if not D[nx][ny] :
                        e += 1
                el, ee, ex, ey = sorted([(el, ee, ex, ey), (l, e, x, y)], key=lambda x : (-x[0], -x[1], x[2], x[3]))[0]
        D[ex][ey] = nums[0]
    for x in range(N) :
        for y in range(N) :
            l = 0
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= N or ny < 0 :
                    continue
                if D[nx][ny] in likes[D[x][y]] :
                    l += 1
            ans += score[l]
    return ans

if __name__ == "__main__" :
    print(solution())