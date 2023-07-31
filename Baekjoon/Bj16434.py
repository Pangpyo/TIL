# 16434 드래곤 앤 던전 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, H = map(int, input().split())
    damage = 0
    maxHp = 0
    for i in range(N) :
        t, a, h = map(int, input().split())
        if t == 1 :
            turn = (h-1)//H
            damage += turn * a
            maxHp = max(maxHp, damage)
        else :
            H += a
            damage = max(0, damage - h)
        
    return maxHp+1

if __name__ == "__main__" :
    print(solution())