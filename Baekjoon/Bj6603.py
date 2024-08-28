# 6603 로또 S2

from itertools import combinations
import sys


def solution():
    input = sys.stdin.readline
    answer = []
    while True:
        temp = input().split()
        if temp[0] == '0':
            break
        S = list(temp[1::])
        S.sort(key=lambda x: int(x))
        for comb in combinations(S, 6):
            answer.append(" ".join(comb))
        answer.append("")
    answer.pop()
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')