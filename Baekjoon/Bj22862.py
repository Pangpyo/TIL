# 22862 가장 긴 짝수 연속한 부분 수열 (large) G5

from collections import deque


def solution() :
    N, K = map(int, input().split())
    que = deque()
    even = 0
    answer = 0
    temp = 0
    nums = list(map(int, input().split()))
    nums.append(1)
    for n in nums :
        if n % 2 :
            if len(que) > K :
                temp -= que.popleft()
            que.append(even)
            temp += even
            even = 0
            answer = max(temp, answer)
        else :
            even += 1
    
    return answer

if __name__ == "__main__" :
    print(solution())