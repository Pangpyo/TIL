# 14467 소가 길을 건너간 이유 1 B1

import sys

sys.stdin = open('input.txt')

N = int(input())
dic = {}
ans = 0
for i in range(N) :
    num, loc = map(int, input().split())
    if num not in dic :
        dic[num] = loc
    elif num in dic and dic[num] != loc :
        dic[num] = loc
        ans += 1
print(ans)