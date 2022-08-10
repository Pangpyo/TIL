# 4963 섬의 개수 S2

import sys


sys.stdin = open('input.txt')


while 1 :
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    seamap = [list(map(int, input().split())) for _ in range(h)] # 지도를 그려줌
    
    def dfs(x, y) :
        dx = [-1, -1, -1, 0, 0, 1, 1, 1] # 8방향으로 검사
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(8) :
            nx = x + dx[i] # 8방향으로 검사함
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w : # 인덱스 초과 방지
                if seamap[nx][ny] == 1 : # 걸어 갈 수 있고 방문하지 않은 땅이 있을 경우
                    seamap[nx][ny] = 2 # 방문 했다는 뜻으로 2로 바꾸어줌
                    dfs(nx, ny) # 방문 한 땅에서 dfs실행
    island = 0
    for i in range(h) :
        for j in range(w) : # 지도의 모든 칸을 검사하며
            if seamap[i][j] == 1 :
                dfs(i, j) # 방문하지 않은 섬이 있을 경우 dfs 함수 실행
                island += 1 # for문 안에서 dfs가 실행 된 횟수가 섬의 개수임
    print(island)