# kakao tech internship 두 큐 합 같게 만들기

from collections import deque




queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

def solution(queue1, queue2):
    half = (sum(queue1) + sum(queue2))/2
    ans = -1
    if half%1 != 0 :
        return ans
    else :
        half = int(half)
    answer = []

    for i in range(len(queue1)-1) :
        dqueue1 = deque(queue1)
        dqueue2 = deque(queue2)
        cnt = 0
        a = deque()
        for _ in range(i) :
            a.append(dqueue1.popleft())
            cnt += 1
        dqueue2 += a
        while sum(dqueue2) <= half :
            dqueue1.append(dqueue2.popleft())
            cnt += 1
        if sum(dqueue1) == sum(dqueue2) == half :
            answer.append(cnt)
    for i in range(len(queue2)-1) :
        dqueue1 = deque(queue2)
        dqueue2 = deque(queue1)
        cnt = 0
        a = deque()
        for _ in range(i) :
            a.append(dqueue1.popleft())
            cnt += 1
        dqueue2 += a
        while sum(dqueue2) <= half :
            dqueue1.append(dqueue2.popleft())
            cnt += 1
        if sum(dqueue1) == sum(dqueue2) == half :
            answer.append(cnt)

    ans = min(answer) if answer else -1
    return ans

print(solution(queue1, queue2))