# 18869 멀티버스 2 G5

from collections import defaultdict
from math import factorial
import sys


def solution() :
    input = sys.stdin.readline
    M, N = map(int, input().split())
    answer = 0
    compressed = defaultdict(int)
    for i in range(M) :
        planets = list(enumerate(map(int, input().split())))
        planets.sort(key = lambda x : (x[1], x[0]))
        dic = defaultdict(int)
        for i, v in planets :
            dic[v] = i
        compStr = ''.join([str(dic[n]) for i, n in planets])
        compressed[compStr] += 1
    for k, v in compressed.items() :
        if v > 1 :
            answer += factorial(v)//(factorial(v-2)*2)
    return answer

if __name__ == "__main__" :
    print(solution())