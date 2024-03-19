# 2370 시장 선거 포스터 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    zips = set()
    for s, e in lines :
        zips.add(s)
        zips.add(e)
    zips = list(zips)
    zips.sort()
    dic = {}
    for i, z in enumerate(zips) :
        dic[z] = i
    wall = [-1]*len(zips)
    for i, line in enumerate(lines) :
        s, e = line
        for j in range(dic[s], dic[e]+1) :
            wall[j] = i
    can_see = set()
    for w in wall :
        if w >= 0 :
            can_see.add(w)
    answer = len(can_see)
    return answer

if __name__ == "__main__" :
    print(solution())