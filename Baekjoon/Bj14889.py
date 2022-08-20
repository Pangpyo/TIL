# 14889 스타트와 링크 S2

from itertools import combinations
import sys


sys.stdin = open('input.txt')

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

teams = list(combinations(list(range(N)), N//2))
ans = []
for t in range(len(teams)//2) :
    start = 0
    link = 0
    for i in range(N//2) :
        for j in range(N//2) :
            start += S[teams[t][i]][teams[t][j]]
            link += S[teams[-1-t][i]][teams[-1-t][j]]
    ans.append(abs(start-link))
print(min(ans))
