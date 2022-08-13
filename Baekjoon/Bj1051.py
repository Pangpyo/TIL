# 1051 숫자 정사각형 S4

import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

square = [list(map(int, input())) for _ in range(N)]

A = max(N, M)
ans = 1
for i in range(N) :
    for j in range(M) : 
        for a in range(1, A) : # 주어진 사각형의 각 칸에서 변의 길이가 1+a인 정사각형들을 그려본다.
            if i+a >= N or j+a >= M : # 인덱스 초과 방지
                continue
            if square[i][j] == square[i+a][j] == square[i][j+a] == square[i+a][j+a] :
            # 정사각형의 각 꼭지점이 같은 경우
                ans = (a+1)**2 if (a+1)**2 >= ans else ans
            # 해당 정사각형의 넓이를 이전의 값과 비교해 더 크면 넣어준다.
print(ans)
