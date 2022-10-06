# 2847 게임을 만든 동준이 S4

import sys

input = sys.stdin.readline  # 입력이 많으므로 표준입력 사용
N = int(input())
levels = []
for i in range(N):
    levels.append(int(input()))  # 레벨 리스트 생성
cnt = 0
for i in range(N - 2, -1, -1):  # 가장 높은 레벨부터 내림차순으로
    if levels[i] >= levels[i + 1]:  # 점수가 다음 레벨 이상인 경우
        cnt += levels[i] - levels[i + 1] + 1  # 다음 레벨보다 1 낮게 만드데 필요한 만큼 cnt +
        levels[i] = levels[i + 1] - 1  # 현재 레벨은 다음 레벨보다 1 낮게 만들어줌
print(cnt)
# 메모리 30840 시간 68
