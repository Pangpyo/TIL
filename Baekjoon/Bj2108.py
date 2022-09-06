# 2108 통계학 S3

import sys


input = sys.stdin.readline

N = int(input())
numl = []
numd = {}
for i in range(N) :
    n = int(input())
    numl.append(n)
    if n not in numd :
        numd[n] = 1
    else :
        numd[n] += 1

numl = sorted(numl)
numd = sorted(numd.items(), key=lambda x : (-x[1], x[0]))


print(round(sum(numl)/N+0.00000000001))
print(numl[N//2])
if N > 1 and numd[0][1] == numd[1][1] :
    print(numd[1][0])
else :
    print(numd[0][0])
print(numl[-1]-numl[0])
