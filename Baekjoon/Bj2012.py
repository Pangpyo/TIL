# 2012 등수 매기기 S3

import sys

input = sys.stdin.readline  # 입력 수가 많으므로 표준입력
N = int(input())
ranks = []  # 예상 등수를 저장
for i in range(N):
    ranks.append(int(input()))
ranks.sort()  # 예상 등수를 오름차순 정령
for i in range(N):
    ranks[i] = abs(ranks[i] - (i + 1))  # 실제 주어질 등수와 예상 등수의 차 저장
print(sum(ranks))  # 합하면 답
# 메모리 52192 시간 654
