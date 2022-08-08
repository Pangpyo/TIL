# 2798 블랙잭 B2

import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())

cards = list(map(int, input().split()))
ans = 0
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) : # 카드 3개의  합의 모든 경우의 수를 계산한다.
            card3 = cards[i]+cards[j]+cards[k] 
            if ans <= card3 <= M : # M보다는 작고, 현재 합보다 클 경우 ans에 저장한다.
                ans = card3
            if ans == M : # 계산 도중 ans가 M과 같을 경우 더 이상 연산을 할 필요가 없으므로 종료한다.
                print(ans)
                exit(0)
print(ans)