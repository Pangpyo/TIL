# 2110 공유기 설치 G4
from bisect import bisect_left as bl
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

P = sorted([int(input()) for _ in range(n)])

s = 1
e = (P[-1] - P[0]) // (m - 1) + 1
# 공유기사이의 최대 거리 사이에 m개의 공유기를 설치하면 거리는 총 m-1개가 나온다. 그러므로 가장 인접한 두 공유기 사이의 거리는 이 값보단 클 것이다.
ans = 0
while s <= e:  # 공유기 사이의 거리 중 최소값을 매개변수로 탐색 시작
    mid = (s + e) // 2
    cnt = 1  # 공유기 개수
    pre = 0  # 0번쨰 집에 하나 설치했다고 가정
    while 1:
        pre = bl(P, mid + P[pre])  # 현재 값으로부터 거리가 mid이상인 값을 이분탐색으로 찾는다
        if pre >= n:  # 인덱스를 넘어갈경우 종료
            break
        else:
            cnt += 1  # 그렇지 않을 경우 공유기 개수 1개 추가
    if cnt >= m:  # 공유기 개수가 m개 이상일 경우 탐색 값을 높여서 탐색
        s = mid + 1
        ans = mid  # 답 최신화
    else:
        e = mid - 1  # 미만일 경우 값을 낮춰서 탐색

print(ans)
