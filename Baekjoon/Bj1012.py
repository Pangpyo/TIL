# 1012 유기농 배추 S2


from collections import deque

for _ in range(int(input())) :
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)] # 빈 필드 생성
    for _ in range(K) :
        y, x = map(int, input().split()) # 배추가 있는 곳 표시
        field[x][y] = 1
    que = deque([]) # popleft를 위해 deque 사용
    dx = [-1, 0, 1, 0] # 상, 우, 하, 좌 순으로 2차원리스트에서 이동시켜줄 변수
    dy = [0, 1, 0, -1]
    worm = 0 # 필요한 벌레의 수
    for i in range(N) : 
        for j in range(M) :
            if field[i][j] == 1 : # 배추가 있는 곳이고 방문하지 않은 곳일 경우
                que.append((i, j)) # 해당 좌표를 que에 더해줌
                field[i][j] = 2 # 방문표시로 해당 좌표의 값을 2로 바꿔줌
                worm += 1 # 벌레의 수 + 1
                while que : 
                    x, y = que.popleft() # 벌레가 놓인 곳에서 갈 수 있는 모든 배추들을 방문
                    for d in range(4) :
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx >= N or nx < 0 or ny >= M or ny < 0 : # 인덱스 초과 방지
                            continue
                        if field[nx][ny] == 1 : # 방문하지 않은 배추일 경우
                            field[nx][ny] = 2 #  방문표시
                            que.append((nx, ny)) # 방문하지 않은 배추에서 다시 다른 곳으로 이동하기 위해 que에 좌표 추가   
    print(worm)
