# 4920 테트리스 게임 G5

import sys

def solution():
    input = sys.stdin.readline
    answer = []
    t = 1
    INF = sys.maxsize
    while True:
        N = int(input())
        if not N:
            break
        blocks = tuple(tuple(map(int, input().split())) for _ in range(N))
        shapes = (
            ((0,0),(0,1),(0,2),(0,3)), 
            ((0,0),(1,0),(2,0),(3,0)), 
            ((0,0),(0,1),(1,1),(1,2)), 
            ((0,1),(1,0),(1,1),(2,0)),
            ((0,0),(0,1),(0,2),(1,2)), 
            ((0,0),(0,1),(1,0),(2,0)),
            ((0,0),(1,0),(1,1),(1,2)),
            ((0,1),(1,1),(2,1),(2,0)),
            ((0,0),(0,1),(1,0),(1,1)), 
            ((0,0),(1,0),(1,1),(2,0)), 
            ((0,1),(1,0),(1,1),(2,1)), 
            ((0,1),(1,0),(1,1),(1,2)), 
            ((0,0),(0,1),(0,2),(1,1)) 
        )
        ans = -INF
        def check_shape(x, y):
            temp = -INF
            for shape in shapes:
                block = 0
                flag = True
                for dx, dy in shape:
                    nx = x + dx
                    ny = y + dy
                    if nx >= N or nx < 0 or ny >= N or ny < 0:
                        flag = False
                        continue
                    block += blocks[nx][ny]
                if flag:
                    temp = max(temp, block)
            return temp
        for i in range(N):
            for j in range(N):
                ans = max(check_shape(i, j), ans)
        answer.append(f'{t}. {ans}')
        t += 1
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')