# 2001 파리 퇴치 D2

import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for i in range(1, T+1) :
    N, M = map(int, input().split()) # 파리가 있는 영역의 넓이와 파리채의 넓이
    flys = [list(map(int, input().split())) for _ in range(N)] # 파리가 있는 영역의 각 파이들의 수
    catch = [[0]*(N-M+1) for _ in range(N-M+1)] # 각 위치별 파리채질 한번으로 잡을 수 있는 파리의 수를 저장할 행렬
    for x in range(N-M+1) :
        for y in range(N-M+1) : # N*N의 영역에서는 총 (N-M+1)*(N-M+1) 만큼의 위치에서 파리채질을 할 수 있다.
            for a in range(x, x+M) : # 각 파리채질마다 잡을 수 있는 파리의 수를 구한다.
                for b in range(y, y+M) :
                    catch[x][y] += flys[a][b]
    ans = 0 
    for row in catch : # 가장 많은 파리를 잡을 수 있는 경우의 파리 수를 구한다.
        if max(row) > ans :
            ans = max(row)

    print('#%d'%i, ans)