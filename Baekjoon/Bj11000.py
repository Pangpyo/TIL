# 11000 강의실 배정 G5

import sys

import heapq

input = sys.stdin.readline
N = int(input())
times = []  # 입력들을 받을 리스트
for i in range(N):
    times.append(tuple(map(int, input().split())))  # 변경할 값이 아니므로 리스트로 넣기보단 튜플형으로 넣어준다.

times.sort()  # 정렬해준다.
rooms = []
heapq.heappush(rooms, times[0][1])  # 가장 앞에있는 값중 하나의 끝나는 시간을 힙푸쉬한다.

for i in range(1, N):
    if (
        times[i][0] < rooms[0]
    ):  # 강의들중 시작시간이 힙큐에 있는 가장 작은 끝나는시간보다 빠른 값이 있다면, 같은 방을 공유 할 수 없는 것이다.
        heapq.heappush(rooms, times[i][1])
    else:  # 반대로 끝나는 시간과 같거나 뒤에 시작한다면, 같은 강의실을 공유할수 있으므로 힙 리플레이스를 사용해 해당 방의 끝나는 시간을 바꿔준다,
        heapq.heapreplace(rooms, times[i][1])
print(len(rooms))  # 총 방의 개수 출력
