# 14465 소가 길을 건너간 이유5 S2

import sys

# 슬라이딩 윈도우
input = sys.stdin.readline

N, K, B = map(int, input().split())

isbroken = [1] * N  # 멀쩡한건 1, 깨진건 0으로 해보자

for i in range(B):
    isbroken[int(input()) - 1] = 0  # 깨진것들만 0으로 바꿔줌


cnt = sum(isbroken[0:K])  # 시작~K개까지의 멀쩡한 신호등 수를 세어줌
ans = cnt  # k개 구간에서 안 깨진 신호등의 최대 개수를 구해보자
for i in range(K, N):  # K부터 한 칸씩 이동해보자
    cnt -= isbroken[i - K]  # 지나간 칸의 값을 하나 빼주고
    cnt += isbroken[i]  # 새로 본 값을 하나 더해주며
    ans = max(ans, cnt)  # 최대값을 갱신
print(K - ans)  # K개에서 K개 구간에서 멀쩡한 신호등의 최대 값을 빼주면 답이 나온다
