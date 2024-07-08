# 24041 성싶당 밀키트 G4

import sys


def solution():
    input = sys.stdin.readline
    N, G, K = map(int, input().split())
    elements = [[], []]
    for _ in range(N):
        S, L, O = map(int, input().split())
        elements[O].append((S, L))

    def get_g(x):
        result = 0
        for speed, limit in elements[0]:
            result += speed*max(1, x-limit)
        elements[1].sort(key=lambda K: -K[0]*max(1, x-K[1]))
        for t in range(K, len(elements[1])):
            speed, limit = elements[1][t]
            result += speed*max(1, x-limit)
        return result

    answer = 0
    s, e = 0, int(2e9)
    while s <= e:
        m = (s+e)//2
        temp = get_g(m)
        if temp <= G:
            s = m + 1
            answer = max(answer, m)
        else: 
            e = m - 1
    return answer

if __name__ == "__main__":
    print(solution())