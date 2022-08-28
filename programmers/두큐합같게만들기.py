# kakao tech internship 두 큐 합 같게 만들기


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

from collections import deque

def solution(queue1, queue2):
    half = (sum(queue1) + sum(queue2))/2
    ans = -1
    if half%1 != 0 :
        return ans
    else :
        half = int(half)
    l = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    cnt = 0
    for _ in range(l*3) :
        if sum1 == half :
            return cnt
        elif sum1 > half :
            t = queue1.popleft()
            queue2.append(t)
            sum1 -= t
            cnt += 1
        else : 
            t = queue2.popleft()
            queue1.append(t)
            sum1 += t
            cnt += 1
    return ans

print(solution(queue1, queue2))