# 7490 0 만들기 G5


from itertools import product
import sys

sign = ["+", "-", " "]

sys.stdin = open("input.txt")


def calculate(pre: list):
    if pre[0] == "+":
        return pre[1]
    else:
        return -pre[1]


T = int(input())
for t in range(T):
    n = int(input())

    signs = list(product(sign, repeat=n - 1))
    answers = []
    for s in signs:
        ans = 0
        pre = ["+", 1]
        for i in range(n - 1):
            if s[i] == " ":
                pre[1] = pre[1] * 10 + i + 2
            else:
                ans += calculate(pre)
                pre = [s[i], i + 2]
        ans += calculate(pre)
        answer = ["1"]
        if ans == 0:
            for i in range(n - 1):
                answer.append(s[i])
                answer.append(str(i + 2))
            answers.append("".join(answer))
    answers.sort()
    print(*answers, sep="\n")
    if t != T - 1:
        print("")
