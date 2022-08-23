# 2304 창고 다각형 S2


import sys

sys.stdin = open('input.txt')

N = int(input()) # 기둥의 개수를 입력받음
walllist = []
maxL = 1 # 기둥들이 있는 칸들을 저장할 리스트
maxH = 1
for _ in range(N) :
    L, H = map(int, input().split()) 
    walllist.append([L,H])
    maxL = L if L > maxL else maxL
    maxH = H if H > maxH else maxH
walls = [0]*(maxL + 1)
for l, h in walllist :
    walls[l] = h # 해당 칸에 H높이의 기둥을 세움

maxHidx = walls.index(maxH)
up = 0 # 시작점에서 가장 높은 기둥까지 가기 위한 인덱스
down = maxL # 끝점에서 가장 높은 기둥까지 가기 위한 인덱스
for i in range(maxHidx+1) : # 시작점~ 가장 높은 벽
    if walls[i] <= walls[up] : # 현재 지붕이 직전의 지붕보다 작을 경우
        walls[i] = walls[up] # 해당 위치에 지붕을 세움
    else :
        up = i # 더 높아질 경우 지붕의 높이 기준을 바꿔줌
for i in range(maxL, maxHidx, -1) : # 끝 점에서 가장 높은 기둥까지
    if walls[i] <= walls[down] : # 위와 같은 작업 반복
        walls[i] = walls[down]
    else :
        down = i
print(sum(walls))