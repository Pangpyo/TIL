# 19639 배틀로얄 G5

import sys


def solution():
    input = sys.stdin.readline
    X, Y, M = map(int, input().split())
    enemys = [int(input()) for _ in range(X)]
    items = [int(input()) for _ in range(Y)]
    idx = 0
    answer = []
    hp = M
    for i, e in enumerate(enemys):
        hp -= e
        answer.append(-i-1)
        while hp <= M//2 and idx < len(items):
            hp += items[idx]
            answer.append(idx+1)
            idx += 1
        if hp <= 0:
            return (0,)
    while idx < len(items):
        answer.append(idx+1)
        idx += 1
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')