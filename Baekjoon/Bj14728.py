# 14728 벼락치기 G5

import sys

# 배낭 문제
input = sys.stdin.readline

N, T = map(int, input().split())

subj = [tuple(map(int, input().split())) for _ in range(N)]

D = [[0] * (T + 1) for _ in range(N + 1)]

for t in range(1, T + 1):  # t시간동안
    for i in range(1, N + 1):  # i개의 과목을 공부할 때의 최대 값을 구해보자
        if t - subj[i - 1][0] >= 0:  # 과목 하나를 더 공부할 시간이 되는 경우
            D[i][t] = max(D[i - 1][t], D[i - 1][t - subj[i - 1][0]] + subj[i - 1][1])
            # 이전까지의 최대값과 이번 과목을 공부할 때 걸리는 시간만큼 뺀 시간에서의 값+이번 과목의 점수를 비교한다
        else:  # 안되는 경우 이전까지의 최대값들중 하나를 뽑아 최대값을 설정한다
            D[i][t] = max(D[i - 1][t], D[i][t - 1])

print(D[-1][-1])  # 마지막 값 출력
