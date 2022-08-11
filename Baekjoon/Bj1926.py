# 1926 그림 S1

import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

def bfs(graph, x, y) :
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1] # 아래, 오른쪽, 위쪽, 왼쪽 순으로 방문 
    area = 1
    graph[x][y] = 2
    queue = [(x, y)] # 방문한 좌표를 저장하고 꺼내올
    while queue :
        x, y = queue.pop(0) # 첫 인덱스의 좌표를 꺼내옴
        for i in range(4) : # 4방향으로 방문
            nx = x + dx[i] # 방문한 후의 좌표 정의
            ny = y + dy[i] # 방문한 후의 좌표 정의
            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                continue # 인덱스가 초과이거나 그림이 아닐 경우 무시
            if graph[nx][ny] == 0 : # 이동 할 칸이 그림이 아닌 경우 무시
                continue
            if graph[nx][ny] == 1 : # 처음 방문 한 칸일 경우
                graph[nx][ny] = 2# 방문의 의미로 2로 바꿔줌
                queue.append((nx, ny)) # 이동한 좌표를 저장
                area += 1 # 한 칸 방문시 마다 넓이 +1
    return area #넓이

picture = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
area = [0] # 그림이 하나도 없는 경우 0을 출력해야하므로 0값을 넣어둔다.
for i in range(N) :
    for j in range(M) :
        if picture[i][j] == 1 :
            area.append(bfs(picture,i,j))
            cnt += 1
print(cnt, max(area), sep='\n')