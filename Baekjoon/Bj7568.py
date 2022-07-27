# 7568 덩치 S5

import sys

sys.stdin = open("input.txt")

N = int(input())
WH = []
for i in range(N) :
    w, h = map(int, input().split()) 
    WH.append((w,h))

for i in range(N) :
    score = 1
    for j in range(N) : 
        if j != i :
            if WH[i][0] < WH[j][0] and WH[i][1] < WH[j][1] :
                score += 1
    print(score, end = ' ')

