# 17612 쇼핑몰 G2

from collections import deque
from heapq import heappop, heappush

N, K = map(int, input().split())

cus = deque([tuple(map(int, input().split())) for _ in range(N)])


heap = []
counter = list(range(1, K + 1))

t = 0
n = 1
ans = 0

while heap or cus:
    while heap:
        t, ct, id = heappop(heap)
        ans += id * n
        n += 1
        heappush(counter, -ct)
        if heap and heap[0][0] != t:
            break
    while cus and counter:
        id, w = cus.popleft()
        heappush(heap, (t + w, -heappop(counter), id))

print(ans)
