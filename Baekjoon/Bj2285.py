# 2285 우체국 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    XA = []
    popul = 0
    for i in range(N) :
        x, a = map(int, input().split())
        popul += a
        XA.append((x, a))
    XA.sort()
    temp = 0
    ans = 0
    for x, a in XA :
        temp += a
        if temp >= popul/2 :
           ans = x 
           break
    return ans

if __name__ == "__main__" :
    print(solution())