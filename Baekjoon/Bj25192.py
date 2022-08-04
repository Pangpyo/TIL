# 25192 인사성 밝은 곰곰이 S4

import sys


sys.stdin = open('input.txt')

N = int(input())
gomgom = 0
loglist = set()
for i in range(N) :
    log = input()
    if log == 'ENTER' :
        gomgom += len(loglist)
        loglist.clear()
    else :
        loglist.add(log)
gomgom += len(loglist)
print(gomgom)