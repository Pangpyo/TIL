# 16236 아기 상어 G3


import sys

sys.stdin = open("input.txt")

N = int(input())
sea = []

for i in range(N):
    s = list(map(int, input().split()))
    if 9 in s:
        w = s.index(9)
        shark = (i, w)  # 상어의 위치
        s[w] = 0  # 상어의 위치를 알았으니 해당 칸을 0으로 만들어줌
    sea.append(s)
size = [2, 2]  # 상어의 크기


def eat():  # 상어가 물고기를 먹었다.
    size[1] -= 1  # 물고기를 하나 먹음
    if size[1] == 0:  # 자기 덩치만큼 먹은 경우
        size[0] += 1  # 1만큼 덩치가 커진다.
        size[1] = size[0]  # 다시 자기 덩치만큼 먹어야한다.


def smallfish():  # 상어보다 작은 물고기의 위치들을 구해줌
    ans = []
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 0:  # 물고기가 없는 칸일 경우 continue
                continue
            if sea[i][j] < size[0]:  # 상어보다 작은 물고기들의 위치를 구해준다.
                ans.append([i, j, 0])  # 0은 추후 상어로부터의 거리가 들어갈 위치이다.
    return ans


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 아래, 오른쪽, 위쪽, 왼쪽 순으로 방문


def bfs(x, y, x1, y1):
    queue = [(x, y)]  # 방문한 좌표를 저장하고 꺼내올
    while queue:
        x, y = queue.pop(0)  # 첫 인덱스의 좌표를 꺼내옴
        for i in range(4):  # 4방향으로 방문
            nx = x + dx[i]  # 방문한 후의 좌표 정의
            ny = y + dy[i]  # 방문한 후의 좌표 정의
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue  # 벽일 경우 무시
            if sea[nx][ny] > size[0]:  # 같거나 큰 물고기가 있는 칸은 지나가지 못함
                continue
            if visit[nx][ny] == 0:  # 처음 방문 한 칸일 경우
                visit[nx][ny] = visit[x][y] + 1  # 직전 칸까지의 이동 거리에서 +1을 해줌
                queue.append((nx, ny))  # 이동한 좌표를 저장
    return visit[x1][y1]  # 이동 시간 반환


second = 0
while 1:
    x, y = shark
    can = False

    eatable = smallfish()  # 먹을 수 있는 생선들의 위치를 모두 구해준다.
    for e in eatable:
        visit = [[0] * N for _ in range(N)]  # 방문함수
        d = bfs(x, y, e[0], e[1])  # 먹을 수 있는 각 생선들까지의 이동 시간을 구해준다.
        e[2] = d  # 이동 시간을 저장해준다
        if d:  # 먹을 수 있는 물고기가 있을 경우 d값 변화
            can = True
    if not can:  # 먹을 수 있는 물고기가 하나도 없을 경우 엄마상어한테 도움을 요청하기 위해 while문 종료
        break
    eatable = sorted(
        eatable, key=lambda x: (x[2], x[0], x[1])
    )  # 상어로부터의 거리, 위에서 가까운순, 왼쪽에서 가까운 순으로 정렬해준다.
    for e in eatable:
        if e[2]:  # e[2]가 0일경우 먹을 수 있는 물고기가 아니다. 0이 아닌 경우중 정렬에 맞는 물고기의 위치와 걸린 시간을 구해준다.
            a, b = e[0], e[1]  # 조건에 맞는 물고기의 위치
            second += e[2]  # 물고기를 먹기까지 걸린 시간을 총 시간에 더해준다.
            break
    eat()  # 조건에 맞는 물고기를 발견 했으니 생선을 먹어준다.
    sea[a][b] = 0  # 물고기가 먹혔으므로 해당 칸은 빈 칸이 된다.
    shark = (a, b)  # 물고기를 먹은 위치가 상어의 새로운 위치이다.
print(second)
