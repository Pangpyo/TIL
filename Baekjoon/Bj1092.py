# 1092 배 G5

from bisect import bisect


N = int(input())
crains = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())))
bp = True
t = 0
if max(boxes) > max(crains):
    print(-1)
else:
    while boxes:
        t += 1
        for i in range(N):
            if not boxes:
                bp = False
                break
            j = bisect(boxes, crains[i])
            if j:
                print(boxes.pop(j - 1))
    print(t)
