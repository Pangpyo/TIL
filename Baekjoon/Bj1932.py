# 1932 정수 삼각형 S1

import sys


input = sys.stdin.readline

n = int(input())

pre = [int(input())]  # 이전의 층에 있는 값들

for i in range(2, n + 1):
    post = list(map(int, input().split()))  # 다음 층에 들어갈 값들
    for j in range(i):
        a = 0
        b = 0
        if j > 0:  # 가장 왼쪽인 경우 예외처리
            a = pre[j - 1]
        if j < i - 1:  # 가장 오른쪽인 경우 예외처리
            b = pre[j]
        post[j] += max(a, b)  # 바로 위의 양 옆 수중 큰 수를 더한다
    pre = post  # 이번 층을 이전 층으로 지정

print(max(pre))  # 마지막 층의 최대값 출력
