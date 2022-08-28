# 2667 단지번호붙이기 S1

from collections import deque
N = int(input())
maps = [list(map(int, input())) for _ in range(N)] # 아파트의 단지를 2차원리스트로 받음
dx = [-1, 0, 1, 0] # 상, 우, 하, 좌 순으로 2차원리스트에서 이동시켜줄 변수
dy = [0, 1, 0, -1]
visit = [[0]*N for _ in range(N)] # 방문처리 할 2차원 리스트
def bfs(x, y, c) : # bfs 함수 선언
    cnt = 1 # 연결된 요소의 개수를 세어줄 함수
    maps[x][y] = c # 단지 번호
    visit[x][y] = 1 # 방문처리
    que = deque([(x, y)]) 
    while que :
        x, y = que.popleft()
        for i in range(4) : # 4방향 방문
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 : # 인덱스 초과 방지
                continue
            if maps[nx][ny] == 0 : # 아파트가 없는 곳은 검사하지 않음
                continue
            if visit[nx][ny] == 0: # 방문하지 않은 곳 방문
                que.append((nx, ny)) # 방문 한 곳에서도 4방향으로 다시 방문하기 위해 que에 추가해줌
                maps[nx][ny] = c # 단지 번호를 붙여줌
                visit[nx][ny] = 1 # 방문처리
                cnt += 1 # 단지의 아파트 수를 세어줌
    return cnt # 연결된 요소의 개수 출력
c = 1 # 단지 시작 번호

homes = []
for x in range(N) :
    for y in range(N) :
        if maps[x][y] != 0 and visit[x][y] == 0 :
            homes.append(bfs(x, y, c))
            c += 1
print(c-1)
homes.sort()
print(*homes, sep = '\n')