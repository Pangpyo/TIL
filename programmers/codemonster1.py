# 1

from itertools import permutations


def solution(marbles):
    answer = []
    n = len(marbles)
    poss = []
    for i in range(1, n + 1):
        per = list(set(permutations(marbles, i)))
        for p in per:
            l = len(p)
            for i in range(l * 2):
                if sum(p[0 : i // 2]) == sum(p[(i + 1) // 2 : :]):
                    rule1 = abs(len(p[0 : i // 2]) - len(p[(i + 1) // 2 : :]))
                    rule2 = len(p)
                    rule3 = sum(p)
                    poss.append((rule1, rule2, rule3, p))
    poss.sort(key=lambda x: (x[0], -x[1], -x[2], x[3]))
    answer = poss[0][3]
    return answer


marbles = [1, 2, 3, 4, 4]

print(solution(marbles))
