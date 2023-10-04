# 1013 Contact G5

import sys
import re

def solution() :
    input = sys.stdin.readline
    T = int(input())
    answers = ['NO']*T
    pattern = r'^(100+1+|01)+$'
    for t in range(T) :
        temp = input().rstrip()
        match = re.fullmatch(pattern, temp)
        if match :
            answers[t] = "YES"
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')