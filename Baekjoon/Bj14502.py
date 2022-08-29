# 14502 연구소 G4

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())


lab = [list(map(int, input().split())) for _ in range(N)] # 연구소를 2차원 리스트로 받음
dx = [-1, 0, 1, 0] # 상하좌우 델타탐색
dy = [0, 1, 0, -1]

def bfs(a, b) : # 바이러스가 너비 우선 탐색으로 퍼져나가는 bfs함수 정의
    que = deque([(a, b)])
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if nlab[nx][ny] == 0 :
                nlab[nx][ny] = 2
                que.append((nx, ny))
virus = [] # 바이러스가 있는 위치 저장
for i in range(N) : 
    for j in range(M) :
        if lab[i][j] == 2 :
            virus.append((i, j))
empty = [] # 빈 공간을 i, j가 아닌 n번째 칸으로 표현
for i in range(N) :
    for j in range(M) :
        if lab[i][j] == 0 :
            empty.append(i*M+j)

walls = list(combinations(empty, 3)) # n번째 칸으로 표현한 빈 칸들의 리스트에서 3개를 뽑아 조합을 만듦
ans = []
for wall in walls : 
    nlab = deepcopy(lab) # 벽을 세워볼 새로운 연구소 생성
    for w in wall :
        nlab[w//M][w%M] = 1 # 벽을 세워줌
    for x, y in virus : # 바이러스들에 대해 bfs실행
        bfs(x, y)
    cnt = 0
    for l in nlab : 
        cnt += l.count(0) # 0, 즉 빈칸의 개수를 세어줌
    ans.append(cnt) # ans에 저장
print(max(ans)) # 빈 칸이 가장 많은 경우 출력