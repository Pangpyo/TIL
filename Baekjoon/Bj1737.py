# 1737 Pibonacci G4

from collections import defaultdict
import math
import sys


def solution() :
    sys.setrecursionlimit(10**9)
    n = int(input())
    pi = math.pi
    dic = defaultdict(int)
    mod = 10**18
    def pibo(n) :
        if n <= pi :
            return 1
        if n in dic :
            return dic[n]
        dic[n] = (pibo(n-1) + pibo(n-pi))%mod
        return dic[n]
    ans = pibo(n)
    return ans

if __name__ == "__main__" :
    print(solution())