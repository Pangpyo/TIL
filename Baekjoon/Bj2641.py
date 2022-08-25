# 2641 다각형그리기 S2

import sys


sys.stdin = open('input.txt')

from copy import deepcopy


N = int(input())
origin = list(map(int, input().split()))
cnt = 0
ans = []
for i in range(int(input())) :
    prob = list(map(int, input().split()))
    nprob = deepcopy(prob)
    nprobr = deepcopy(prob[::-1])
    for n in range(N) :
        if nprobr[n] == 1 :
            nprobr[n] = 3
        elif nprobr[n] == 2 :
            nprobr[n] = 4
        elif nprobr[n] == 3 :
            nprobr[n] = 1
        elif nprobr[n] == 4 :
            nprobr[n] = 2
    for _ in range(N) :
        a = nprob.pop(0)
        nprob.append(a)
        if origin == nprob :
            cnt += 1
            ans.append(prob)
            break
    for _ in range(N) : 
        a = nprobr.pop(0)
        nprobr.append(a)
        if origin == nprobr :
            cnt += 1
            ans.append(prob)
            break
print(cnt)
for a in ans :
    print(*a)
