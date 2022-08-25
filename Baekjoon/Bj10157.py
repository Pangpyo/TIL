# 10157 자리배정 S4



C, R = map(int, input().split())
# C가 세로, R이 가로로 회전해서 생각
seat = [[0]*R for _ in range(C)]
d = 0
c = 0
r = 0
ans = False
K = int(input())
for i in range(1, C*R+1) :
    if d == 0 :
        seat[c][r] = i
        if r >= R-1 or seat[c][r+1] != 0 :
            d = (d+1)%4
            c += 1 # 방향을 회전해야 할 경우, 아래쪽으로 진행
        else :
            r += 1 # 오른쪽으로 진행

    elif d == 1 :
        seat[c][r] = i 
        if c >= C-1 or seat[c+1][r] != 0 :
            d = (d+1)%4
            r -= 1 # 방향을 회전해야 할 경우, 왼쪽으로 진행
        else :
            c += 1  # 아래쪽으로 진행
    elif d == 2 :
        seat[c][r] = i 
        if r <= 0 or seat[c][r-1] != 0 :
            d = (d+1)%4
            c -= 1 # 방향을 회전해야 할 경우, 위쪽으로 진행
        else :
            r -= 1 # 왼쪽으로 진행
    else : 
        seat[c][r] = i 
        if c <= 0 or seat[c-1][r] != 0 :
            d = (d+1)%4
            r += 1 # 방향을 회전해야 할 경우, 아래쪽으로 진행
        else :
            c -= 1 # 위쪽으로 진행

for i in range(C) :
    for j in range(R) :
        if seat[i][j] == K :
            ans = (i+1, j+1)
            break
if ans :
    print(*ans)
else :
    print(0)