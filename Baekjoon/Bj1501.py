# 1501 영어 읽기 G5

from collections import defaultdict
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    dic = defaultdict(int)
    for _ in range(N) :
        word = input().rstrip()
        dic[("".join(sorted(word)), word[0]+word[-1])] += 1
    M = int(input())
    answers = [1]*M

    for m in range(M) :
        for word in input().split() :
            answers[m] *= dic[("".join(sorted(word)), word[0]+word[-1])]
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')