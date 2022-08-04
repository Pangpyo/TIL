# 2669 직사각형 네개의 합집합의 면적 구하기 B1

import sys

sys.stdin = open('input.txt')
# 해당하는 좌표들을 색칠한다는 개념으로 접근했다.
coordi = [[0]*100 for _ in range(100)]
# 문제에서 주어진 범위의 좌표평면을 설정한다.
for _ in range(4) :
    i, j, x, y = map(int, input().split())
    for a in range(i, x) :
        for b in range(j, y) : # 해당하는 범위들의 값을 1로 바꿔준다.
            coordi[a][b] = 1
print(sum(map(sum, coordi))) #좌표평면에 존재하는 값들을 모두 더해준다.