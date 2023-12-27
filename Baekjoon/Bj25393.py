# 25393 교집합 만들기 G5

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    starts = defaultdict(list)
    ends = defaultdict(list)
    sets = defaultdict(set)
    for _ in range(N) :
        l, r = map(int, input().split())
        starts[l].append(r)
        ends[r].append(l)
        sets[l].add(r)
    for s, e in zip(starts.keys(), ends.keys()) :
        starts[s].sort()
        ends[e].sort()
    Q = int(input())
    answers = [-1]*Q
    for q in range(Q) :
        l, r = map(int, input().split())
        if starts[l] and ends[r] :
            if l in sets and r in sets[l] :
                answers[q] = 1
            elif starts[l][-1] >= r and ends[r][0] <= l:
                answers[q] = 2
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')