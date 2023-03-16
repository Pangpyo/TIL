from heapq import heappop, heappush


def solution(N, coffee_times):
    heap = []
    answer = []
    time = 0
    for i, v in enumerate(coffee_times):
        if len(heap) >= N:
            time, n = heappop(heap)
            answer.append(n)
        heappush(heap, (v + time, i + 1))
    while heap:
        time, n = heappop(heap)
        answer.append(n)
    return answer


coffee_times = [4, 2, 2, 5, 3]

print(solution(3, coffee_times))
