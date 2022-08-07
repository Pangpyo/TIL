# 1948 날짜 계산기 D2

import sys

sys.stdin = open('input.txt')

T = int(input())
def month(m) : # 해당 달의 일수를 반환해줄 함수
    day31 = [1, 3, 5, 7, 8, 10, 12] 
    day30 = [4, 6, 9, 11]
    if m in day31 :
        return 31
    elif m in day30 :
        return 30
    else : # 2월
        return 28
for t in range(1, T+1) :
    m1, d1, m2, d2 = map(int, input().split()) 
    days = 0
    for m in range(m1, m2) : # 주어진 날짜의 첫째달~ 마지막달-1까지의 일수를 모두 더해줌
        days += month(m)
    days += d2 - d1 +1 # 마지막 달의 일 d2를 더해주고 첫째달의 d1을 빼준 후 1을 더해줌
    print('#%d'%t, days)