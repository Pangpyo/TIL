# 1769 3의 배수 S5

import sys
input = sys.stdin.readline
cnt = 0
n = int(input())
while n > 10 :
    nx = 0
    cnt += 1
    for i in list(map(int, str(n))):
        nx += i
    n = nx
if n < 10 :
    if n%3 == 0 :
        print(cnt, "YES", sep='\n')
    else :
        print(cnt, "NO", sep='\n')