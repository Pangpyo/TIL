# 1132 합 G3

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

dic = defaultdict(int)
zdic = defaultdict(int)
notzero = set()

for i in range(N):
    temp = input().rstrip()
    l = len(temp)
    notzero.add(temp[0])
    for i in range(1, l + 1):
        dic[temp[i - 1]] += 10 ** (l - i)

dic = sorted(dic.items(), key=lambda x: x[1])

l = len(dic)

z = ()
for i in range(l):
    k, v = dic[i]
    if l == 10 and k not in notzero:
        dic.pop(i)
        dic.insert(0, (k, v))
        break

ans = 0
n = 9
for i, v in reversed(dic):
    if not n:
        break
    ans += n * v
    n -= 1

print(ans)
