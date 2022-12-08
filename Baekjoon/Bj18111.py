# 18111 마인크래프트 S2

import sys


sys.stdin = open("input.txt")

N, M, B = map(int, input().split())


ground = [list(map(int, input().split())) for _ in range(N)]  # 땅의 높낮이 저장

low = min(map(min, ground))  # 땅의 최소높이
high = max(map(max, ground))  # 땅의 최고높이

ans = []
height = [0] * (257)  # 각 높이에 해당하는 땅이 몇개인지

for i in range(N):
    for j in range(M):
        height[ground[i][j]] += 1


def flatten(h):  # 땅을 h높이로 만드려한다
    global B, low, high
    blocks = B  # 인벤토리에 가지고있는 블럭의 개수
    t = 0  # 시간
    for i in range(low, high + 1):
        if not height[i]:  # 해당 높이의 땅이 없으면 continue
            continue
        diff = i - h  # 땅의 높이와 원하는 높이의 차이
        if diff > 0:
            blocks += diff * height[i]  # 땅이 더 높은경우 블럭을 얻음
            t += 2 * diff * height[i]  # 그 2배만큼 시간이 지나감
        elif diff < 0:
            blocks += diff * height[i]  # 땅이 더 낮은 경우 그 만큼 블럭을 잃음(diff가 음수)
            t -= diff * height[i]  # 그만큼 시간이 지나감
    if blocks >= 0:  # 이후 가지고있는 블럭의 개수가 0 미만인 경우는 불가능한 경우이므로 0이상인 경우만 추가
        ans.append((t, h))


for h in range(low, high + 1):  # 가장 낮은 높이부터 가장 높은 높이까지 모든 경우로 평탄화 시켜본다
    flatten(h)
ans.sort(key=lambda x: (x[0], -x[1]))  # 시간 오름차순, 높이 내림차순으로 정렬
print(*ans[0])
