# 23843 콘센트 G5

import heapq


N, M = map(int, input().split())
things = sorted(
    list(map(int, input().split())), reverse=True
)  # 충전시간이 긴 기기부터 충전하기 위해 정렬한다.
sockets = [0] * M  # 콘센트의 개수.
heapq.heapify(sockets)  # 힙으로 바꿔준다
for thing in things:
    heapq.heappush(
        sockets, thing + heapq.heappop(sockets)
    )  # 콘센트의 어떤 칸에서 기기들이 충전한 총 시간을 구해준다. 그러기 위해 이전에 충전했던 기기의 충전시간 + 충전할 기기의 충전시간을 더해 힙 푸쉬해준다.
    # 매번 힙과 푸쉬를 한 번씩 하기에, sockets의 개수는 M개로 유지된다.
# 예시 8 4 4 1 1
# 0 0
# 0 8
# 4 8
# 8 8
# 8 9
# 9 9
print(max(sockets))
