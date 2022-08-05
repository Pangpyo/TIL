# 1979 어디에 단어가 들어갈 수 있을까 D2

import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for i in range(1,T+1) :
    N, K = map(int, input().split())
    puzzl = [list(map(int, input().split())) for _ in range(N)] # 퍼즐을 행렬로 입력받음
    ans = 0
    for x in range(N) :
        row = 0 # 행과 열의 빈칸을 세어줄 변수 설정
        col = 0
        for y in range(N) : 
            if puzzl[x][y] == 1 : # 1일경우 빈 칸이므로 row에 +1
                row += 1
            if puzzl[x][y] == 0 or y == N-1: 
            # 0일경우나 가장 끝 인덱스를 검사하는 경우 이전까지의 빈칸의 개수를 세어준 후, 
            # 단어의 길이와 같으면 답에 +1
                if row == K :
                    ans += 1
                row = 0
            if puzzl[y][x] == 1 : # 열에 대해서도 같은 작업 반복
                col += 1
            if puzzl[y][x] == 0 or y == N-1:
                if col == K :
                    ans += 1
                col = 0
    print('#%d'%i, ans)
