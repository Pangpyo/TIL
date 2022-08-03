# 2167 2차원 배열의 합 B1

import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split()) # 행과 열의 갯수를 입력받는다

matrix = [list(map(int, input().split())) for _ in range(N)]
# 2차원 리스트를 입력받는다

K = int(input())
# 합을 구할 부분의 개수를 입력받는다
for _ in range(K) :
    ans = 0 # 총 합을 저장할 변수를 지정한다.
    i, j, x, y = map(int, input().split()) 
# 시작 좌표 (i,j)와 끝 좌표 (x,y)를 입력받는다.
    for k in range(i-1, x) : # i번째~x번째 행을 검사
        ans += sum(matrix[k][j-1:y]) # 각 행의 j번째~y번쨰 인덱스들을 더해줌
    print(ans) # 더한 값을 출력
