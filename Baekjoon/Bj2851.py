# 2851 슈퍼마리오 B1
import sys

sys.stdin = open("input.txt")

total = []
score = 0
for i in range(10) :
    mush = int(input())
    score += mush
    total.append(score)
total_dif = []
for i in total :
    total_dif.append(abs(i-100))

a = total_dif[::-1].index(min(total_dif))

print(total[9-a])