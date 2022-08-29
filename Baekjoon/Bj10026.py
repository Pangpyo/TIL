# 10026 적록색약 G5

from collections import deque
import sys


sys.stdin = open('input.txt')

N = int(input())

picture = [list(input()) for _ in range(N)] # 그림 색들을 리스트로 받아줌
visit = [[False]*N for _ in range(N)] # 방문 리스트
dx = [-1, 0, 1, 0] # 델타탐색
dy = [0, 1, 0, -1]

def bfs(x, y) : # 같은 색들의 구역을 탐색해줄 bfs 함수 생성
    que = deque([(x, y)])
    color = picture[x][y]
    visit[x][y] = True
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            if visit[nx][ny] : # 방문하지 않은 칸에 대하여
                continue
            if picture[nx][ny] == color : # 같은 색일 경우 방문처리
                visit[nx][ny] = True
                que.append((nx, ny)) # 방문 할 칸을 큐에 추가

cnt = 0 # 구역의 개수가 몇개인지, 즉 bfs의 실행 회수가 몇번인지 세어줌
ans = []
for i in range(N) :
    for j in range(N) :
        if not visit[i][j] :
            bfs(i, j)
            cnt += 1
ans.append(cnt)

for i in range(N) : # 적록색맹이 보는 그림으로 바꿔줌
    for j in range(N) :
        if picture[i][j] == 'G' :
            picture[i][j] = 'R'
visit = [[False]*N for _ in range(N)] # 방문리스트와 구역의 개수 초기화
cnt = 0

for i in range(N) : # 적록색맹이 보는 그림에 대하여 구역의 개수를 세어줌
    for j in range(N) :
        if not visit[i][j] :
            bfs(i, j)
            cnt += 1
ans.append(cnt)

print(*ans) # 답 출력
