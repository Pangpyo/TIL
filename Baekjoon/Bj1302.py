# 1302 베스트셀러 S4

import sys

sys.stdin = open('input.txt')

n = int(input())

sell_list = {}
for i in range(n) :
    book = input()
    if book not in sell_list :
        sell_list[book] = 1
    else :
        sell_list[book] += 1
result = [k for k, v in sell_list.items() if v == max(sell_list.values())]
result.sort()

print(result[0])

