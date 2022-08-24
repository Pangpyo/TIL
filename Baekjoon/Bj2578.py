# 2578 빙고 S4

import sys


sys.stdin = open('input.txt')

chul = [list(map(int, input().split())) for _ in range(5)]

mc = [list(map(int, input().split())) for _ in range(5)]

def bingo() :
    ans = 0
    for i in range(5) :
        if sum(chul[i]) == -5 :
            ans += 1
        if chul[0][i]+chul[1][i]+chul[2][i]+chul[3][i]+chul[4][i] == -5 :
            ans += 1
    updiag = 0
    downdiag = 0
    for i in range(5) :
        updiag += chul[i][i]
        downdiag += chul[i][-i-1]
    if updiag == -5 :
        ans += 1
    if downdiag == -5 :
        ans += 1
    return ans
def findnum(n) :
    for i in range(5) :
        for j in range(5) :
            if chul[i][j] == n :
                chul[i][j] = -1
gameend = 0
for i in range(5) :
    for j in range(5) :
        findnum(mc[i][j])
        ans = bingo()
        if ans >= 3 :
            print(5*i+j+1)
            gameend = 1
            break
    if gameend == 1 :
        break