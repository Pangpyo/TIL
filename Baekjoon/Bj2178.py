# 2178 미로탐색 S1


import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

def bfs(graph, x, y) :
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1] # 아래, 오른쪽, 위쪽, 왼쪽 순으로 방문 
    N = len(graph) # 행
    M = len(graph[0]) # 열
    queue = [(x, y)] # 방문한 좌표를 저장하고 꺼내올
    while queue :
        x, y = queue.pop(0) # 첫 인덱스의 좌표를 꺼내옴
        for i in range(4) : # 4방향으로 방문
            nx = x + dx[i] # 방문한 후의 좌표 정의
            ny = y + dy[i] # 방문한 후의 좌표 정의
            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                continue # 벽일 경우 무시
            if graph[nx][ny] == 0 : # 이동 할 수 없는 칸일 경우 무시
                continue
            if graph[nx][ny] == 1 : # 처음 방문 한 칸일 경우
                graph[nx][ny] = graph[x][y] + 1 # 직전 칸까지의 이동 거리에서 +1을 해줌
                queue.append((nx, ny)) # 이동한 좌표를 저장
    return graph[-1][-1] # N, M의 값 반환

miro = [list(map(int, input())) for _ in range(N)]

print(bfs(miro,0,0))