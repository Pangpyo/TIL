# C번 미팅
# 알고리즘 분류 : dp, 배낭 문제
# 예상 난이도 : 골드5~4

from pprint import pprint
import sys


sys.stdin = open("input.txt")

n, m, c = map(int, input().split())

W = [list(map(int, input().split())) for _ in range(c)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = [[0] * (m + 1) for _ in range(n + 1)]
# 최대 만족도를 저장할 리스트. 인덱스 초과 방지를 위해 열과 행을 한개씩 더 생성한다

q = [[0] * m for _ in range(n)]

for i in range(1, n + 1):
    a = A[i - 1] - 1  # A대학의 i번쨰 학생의 성격유형
    for j in range(1, m + 1):
        b = B[j - 1] - 1  # B대학의 j번째 학생의 성격유형
        q[i - 1][j - 1] = W[a][b]
        D[i][j] = max(D[i - 1][j - 1] + W[a][b], D[i][j - 1], D[i - 1][j])
        # D그래프를 기준으로 대각선 + i j 학생의 만족도, 왼쪽, 위쪽중 최대값을 구한다


pprint(q)
pprint(D)
print(D[-1][-1])  # 최대값 출력
