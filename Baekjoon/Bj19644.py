# 19644 좀비 떼가 기관총 진지에도 오다니 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    L = int(input())
    ml, mk = map(int, input().split())
    C = int(input())
    Z = [int(input()) for _ in range(L)]
    shoot = deque()
    for i in range(L) :
        if shoot and shoot[0] <= i :
            shoot.popleft()
        if Z[i] <= len(shoot)*mk + mk :
            shoot.append(i+ml)
        else :
            if C :
                C -= 1
            else :
                return "NO"
        
    return "YES"

if __name__ == "__main__" :
    print(solution())