# 13904 과제 G3

from collections import deque
import heapq


N = int(input())
homework = []
for i in range(N):
    homework.append(tuple(map(int, input().split())))

homework = deque(sorted(homework))
todo = []
done = []
i = 1
ans = 0
while homework:
    # print(i, homework)
    while homework and homework[0][0] == i:
        day, score = homework.popleft()
        heapq.heappush(todo, (-score, day))
    # print("todo", todo)
    while i > len(done) and todo:
        score, day = heapq.heappop(todo)
        if day >= i:
            heapq.heappush(done, (-score, day))
        # print("done", done)
    while todo:
        if -todo[0][0] >= done[0][0]:
            score, day = heapq.heappop(todo)
            heapq.heappop(done)
            heapq.heappush(done, (-score, day))
        else:
            break
    i += 1
    # print("done", done)

for score, day in list(done):
    ans += score
print(ans)
