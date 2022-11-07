# 1759 암호 만들기 G5

from itertools import combinations

L, C = map(int, input().split())

V = ["a", "e", "i", "o", "u"]

chars = list(input().split())
chars.sort()

coms = combinations(chars, L)
for com in coms:
    vowels = 0
    for c in com:
        if c in V:
            vowels += 1
    if 1 <= vowels <= L - 2:
        print("".join(com))
