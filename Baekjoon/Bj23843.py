# 23843 콘센트 G5

import heapq


N, M = map(int, input().split())

things = sorted(list(map(int, input().split())))  # 충전시간이 긴 기기부터 충전하기 위해 정렬한다.

sockets = []  # 충전중인 기기
t = 0  # 시간
while 1:
    while sockets and sockets[0] == t:  # 충전이 다 된 기기들을 소켓에서 모두 빼준다.
        heapq.heappop(sockets)
    if not sockets and not things:  # 대기중인 기기도 없고, 충전중인 기기도 없을 경우 종료
        break
    while things and len(sockets) < M:  # 소켓에 빈 공간이 있을경우 빈 공강만큼 채워준다.
        heapq.heappush(sockets, things.pop() + t)  # 충전시간 + 현재 시간을 힙 푸쉬한다.
    t += 1
print(t)
