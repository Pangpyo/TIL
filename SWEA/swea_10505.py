# 10505. 소득 불균형 D3

import sys

sys.stdin = open("_소득불균형.txt")

T = int(input()) 

for i in range(1,T+1) :
    n = int(input())
    N = list(map(int, input().split())) 
    mean = sum(N)/n # 리스트의 평균을 구했다.
    ans = 0
    for j in N :
        if j <= mean : # 평균 이하의 값을 세어주었다.
            ans += 1
    print('#%d'%i, ans)