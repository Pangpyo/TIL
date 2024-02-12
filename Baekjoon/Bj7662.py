# 7662 이중 우선순위 큐 G4

from collections import defaultdict
from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    EMPTY = "EMPTY"
    answers = [EMPTY]*T
    for t in range(T) :
        k = int(input())
        maxque = []
        minque = []
        dic = defaultdict(int)
        for _ in range(k) :
            l, n = input().split()
            n = int(n)
            if l == "I" :
                if not dic[n] :
                    heappush(minque, n)
                    heappush(maxque, -n)
                dic[n] += 1
            else :
                if n == 1 :
                    if maxque :
                        dic[-maxque[0]] -= 1
                else :
                    if minque :
                        dic[minque[0]] -= 1
                while maxque :
                    if not dic[-maxque[0]] :
                        heappop(maxque)
                    else :
                        break
                while minque :
                    if not dic[minque[0]] :
                       heappop(minque)
                    else :
                        break 
        if maxque :
            answers[t] = str(-maxque[0]) + " " + str(minque[0])
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')