# 2866 문자열 잘라내기 G5


import sys


input = sys.stdin.readline


def answer():
    r, c = map(int, input().split())
    inword = [list(input().rstrip()) for _ in range(r)]
    word = sorted([[inword[-i - 1][j] for i in range(r)] for j in range(c)])
    cnt = 0
    for i in range(r):
        nword = []
        word[0].pop()
        nword.append(word[0])
        for j in range(1, c):
            word[j].pop()
            if word[j] == nword[-1]:
                return cnt
            nword.append(word[j])
        word = nword
        cnt += 1
    return cnt


print(answer())
