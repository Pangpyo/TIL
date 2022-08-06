# 1859. 백만 장자 프로젝트 D2


import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(1,T+1) :
    n = int(input())
    price = list(map(int, input().split()))
    money = 0
    goods = 0
    while price :
        sell = price.index(max(price))
        goods = len(price[0:sell])
        money += -sum(price[0:sell]) + goods*price[sell]
        price = price[sell+1::]
    print('#%d'%i, money)