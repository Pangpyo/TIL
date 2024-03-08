# 27896 특별한 서빙 G5

from heapq import heappop, heappush


def solution() :
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    score = 0
    heap = []
    answer = 0
    for x in X :
        heappush(heap, -x)
        score += x
        if score >= M :
            x = -heappop(heap)
            score -= x*2
            answer += 1
    
    return answer
if __name__ == "__main__" :
    print(solution())