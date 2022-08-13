# 3499. 퍼펙트 셔플 D3

import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for i in range(1, T+1) :
    N = int(input())
    cards = list(input().split())
    cardbot = cards[0:(N+1)//2] # 아래에 놓을 카드와 위에 놓을 카드를 분리한다. 카드 수가 홀수인 경우 아래에 한 장 더 높기 위해 N+1//2까지 범위를 설정했다.
    cardtop = cards[(N+1)//2::]
    cardshu = []
    for j in range(N) :
        if j%2 == 0 :
            cardshu.append(cardbot.pop(0)) # 아래에 놓을 카드와 위에 놓을 카드에서 번갈아가며 셔플에 넣어준다.
        else :
            cardshu.append(cardtop.pop(0))
    print('#%d'%i, *cardshu)