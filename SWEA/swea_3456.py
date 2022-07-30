# 3456. 직사각형 길이 찾기 D3

import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for i in range(1, T+1) :
    squar = list(map(int, input().split()))
    for j in squar :
        if squar.count(j) != 2 :  # 2개의 짝지어진 변이 아닌 경우의 변의 길이를 구해야한다.
            print('#%d'%i, j) # 정사각형의 경우가 있으므로 한 번 출력하면 바로 break로 for문을 빠져나온다.
            break
