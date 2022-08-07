# 1954 달팽이 숫자 D2

import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    snail = [[0]*N for _ in range(N)] # N*N의 0행렬이다.
    i = 0
    j = 0
    quad = 0 # 달팽이 숫자의 진행방향을 상하좌우로 나눌 변수이다.
    for n in range(1, N*N+1) :
        snail[i][j] = n
        if quad%4 == 0 : #오른쪽으로 진행할 경우이다.
            if j == N-1 or snail[i][j+1]: #진행 중 가장 끝에 닿거나, 0이 아닌 곳에 닿을경우
                quad += 1 # 다음 방향으로 진행한다.
                i += 1 # 다음 방향으로 1칸 이동
            else :
                j += 1 # 같은 방향으로 갈 경우 해당 방향으로 1칸 이동
        elif quad%4 == 1 : # 아래로 진행 할 경우
            if i == N-1 or snail[i+1][j]: 
                quad += 1
                j -= 1
            else :
                i += 1
        elif quad%4 == 2 : # 왼쪽으로 진행 할 경우
            if j == 0 or snail[i][j-1] :
                quad += 1
                i -= 1
            else :
                j -= 1
        else : # 오른쪽으로 진행 할 경우
            if i == 0 or snail[i-1][j] :
                quad += 1
                j += 1
            else :
                i -= 1
    print('#%d'%t) # 테스트케이스 번호
    for k in range(N) : # 행렬을 출력
        print(*snail[k])

