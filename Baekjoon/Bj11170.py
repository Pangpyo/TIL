# 11170 0의 개수 B1

import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(T) :
    N, M = map(int, input().split())
    ans = 0
    for j in range(N, M+1) :
        ans += str(j).count('0') # 스트링으로 변환 후 0의 갯수를 세어줌
        
    print(ans)