# 1011 Fly me to the Alpha Centauri G5

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    for t in range(T) :
        x, y = map(int, input().split())
        d = y-x
        n = int(d**0.5)
        more = (d-n*n)//n + (1 if (d-n*n)%n else 0)
        
        answer[t] = n*2-1 + more
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')