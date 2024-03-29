# 13904 과제 G3

from collections import deque
import heapq


N = int(input())
homework = []
for i in range(N):
    homework.append(tuple(map(int, input().split())))  # 과제 정보를 리스트 안에 튜플로 저장

homework = deque(sorted(homework))  # 날짜순으로 정렬 후 덱으로 바꿔준다
todo = []  # 해당 날짜까지가 데드라인인 과제들이 들어갈 우선순위 큐 (점수가 큰 순)
done = []  # 최종적으로 해야하는 과제들이 들어갈 우선순위 큐
i = 1  # 날짜
while homework:  # 모든 과제들의 제출 기간이 끝날 때 까지
    while homework and homework[0][0] == i:  # 해당 날짜에 제출해야만 하는 과제들을 모두 todo로 보낸다.
        day, score = homework.popleft()
        heapq.heappush(todo, (-score, day))  # 우선순위 큐에서 오름차순으로 정렬하기 위해, -를 붙인다.
    while i > len(done) and todo: # 한 과제의 수가 날짜보다 적은 경우(하루에 하나씩만 할 수 있으므로) 해야 할 과제가 목록에 있을 경우 
        score, day = heapq.heappop(todo) # 해야 할 과제를 하나 꺼내
        if day >= i: # 마감이 안 지났을 경우에만 한 과제 목록에 넣어준다.
            heapq.heappush(done, (-score, day))
    while todo: # 해야 할 일 목록에 현재 한 과제보다 점수가 높은 과제가 있을 경우 교체해준다.
        if -todo[0][0] >= done[0][0]:
            score, day = heapq.heappop(todo)
            heapq.heappop(done)
            heapq.heappush(done, (-score, day))
        else:
            break
    i += 1
ans = 0  # 총 점수
for score, day in list(done):
    ans += score
print(ans)
