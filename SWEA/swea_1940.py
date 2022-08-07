# 1940 가랏! RC카! D2

import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1) :
    N = int(input())
    speed = 0
    dis = 0
    for j in range(N) :
        comm = list(map(int, input().split()))
        if comm[0] == 1 : # 가속시
            speed += comm[1]
        elif comm[0] == 2 : #감속시
            speed -= comm[1]
            if speed < 0 :  # 속도가 -가 될수 없으므로 감속 후 속도가 음수인 경우 0으로 맞춰준다.
                speed = 0
        dis += speed # 1초간 이동한 거리만큼 이동거리에 더해줌
    print('#%d'%i, dis)
