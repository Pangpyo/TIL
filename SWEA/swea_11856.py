# 11856. 반반 D3

import sys

sys.stdin = open("_반반.txt")

T = int(input())

for i in range(1, T+1) :
    S = input()
    cnt = 0
    for char in S :
        if S.count(char) != 2 :
            cnt = 1
    ans = 'Yes' if cnt == 0 else 'No'
    print('#%d'%i, ans)
    