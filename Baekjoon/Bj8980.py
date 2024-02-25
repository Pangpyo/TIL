# 8980 택배 G2

import sys
from heapq import heappop, heappush
def solution() :
    input = sys.stdin.readline

    N, C = map(int, input().split())
    M = int(input())
    boxes = sorted([tuple(map(int, input().split())) for _ in range(M)])


    heap = []
    put = [0] * (N + 1)
    have = 0
    j = 0
    ans = 0
    for i in range(1, N + 1):
        C += put[i]
        while j < M and boxes[j][0] == i:
            s, e, c = boxes[j]
            if have + c <= C:
                heappush(heap, (-e, c))
                put[e] += c
                have += c
            else:
                if -heap[0][0] <= e:
                    if C - have != 0:
                        heappush(heap, (-e, (C - have)))
                        put[e] += C - have
                        have = C
                elif -heap[0][0] > e:
                    while -heap[0][0] > e:
                        oe, oc = heappop(heap)
                        put[-oe] -= oc
                        have -= oc
                        if have + c > C:
                            if not heap or -heap[0][0] <= e:
                                heappush(heap, (-e, (C - have)))
                                put[e] += C - have
                                have += C - have
                            else:
                                pass
                        else:
                            heappush(heap, (-e, c))
                            put[e] += c
                            have += c
                            if have < C:
                                heappush(heap, (oe, (C - have)))
                                put[-oe] += C - have
                                have = C
                        if have == C:
                            break
            j += 1
        ans += put[i]

    return ans

if __name__ == "__main__" :
    print(solution())
