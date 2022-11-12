# 코드몬스터3

from itertools import combinations


def solution(reference, track):
    n = len(reference)
    m = len(track)
    jumps = []
    for i in range(1, n + 1):
        com = list(set(combinations(reference, i)))
        for c in com:
            jumps.append("".join(c))
    answer = m
    while track:
        for i in range(1, len(track) + 1):
            if track[0:i] in jumps:
                cut = i
            else:
                break
        print(len(track[0:cut]), track[0:cut])
        answer = min(answer, len(track[0:cut]))
        track = track[cut::]
    return answer


reference = "abc"
track = "bcab"

print(solution(reference, track))
