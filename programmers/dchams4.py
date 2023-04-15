from heapq import heappop, heappush


def solution(N, T):
    bit_time = [63, 6, 91, 79, 102, 109, 124, 7, 127, 111]
    time_bit = {63: 0, 6: 1, 91: 2, 79: 3, 102: 4, 109: 5, 124: 6, 7: 7, 127: 8, 111: 9}

    def time_flow(t):
        t[3] += 1
        if t[3] == 10:
            t[3] = 0
            t[2] += 1
        if t[2] == 6:
            t[2] = 0
            t[1] += 1
        if t[1] == 10:
            t[1] = 0
            t[0] += 1
        if t[0] == 2 and t[1] == 4:
            t[0] = 0
            t[1] = 0
        return tuple(t)

    S = [0, 0, 0, 0]
    for i, n in enumerate(N):
        for j, t in enumerate(n):
            if t:
                S[i] |= 1 << j
    S = tuple(time_bit[i] for i in S)
    T = tuple(T)
    print(S, T)
    answer = 0
    que = []
    heappush(que, (0, *S))
    visit = set()
    visit.add(S)
    while que:
        d, tt, t, mm, m = heappop(que)
        ntimes = time_flow([tt, t, mm, m])
        if ntimes not in visit:
            heappush(que, (d + 1, *ntimes))
            visit.add(ntimes)
            if ntimes == T:
                answer = d + 1
                break
        ntimes = (tt, t, 0, 0)
        if ntimes not in visit:
            heappush(que, (d + 2, *ntimes))
            visit.add(ntimes)
            if ntimes == T:
                answer = d + 2
                break
    return answer


N = [
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
]
T = [0, 0, 5, 8]

print(solution(N, T))
