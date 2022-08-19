# 2116 주사위 쌓기 G4

import sys

sys.stdin = open('input.txt')

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

def dicematch(x) :
    if x == 0 :
        return 5
    elif x == 1 :
        return 3
    elif x == 2 :
        return 4
    elif x == 3 :
        return 1
    elif x == 4 :
        return 2
    else :
        return 0
maxsum = 0
def maxside(list, b) :
    ans = 0
    t = dicematch(b)
    for i in list :
        if i in [b, t] :
            pass
        else :
            ans = i if i > ans else ans
    return ans

for j in range(3) :
    sum = 0
    bot = dices[0][j]
    top = dices[0][dicematch(j)]
    sum += maxside(dices[0], bot)
    for i in range(1, n) :
        botidx = dices[i].index(top)
        bot = dices[i][botidx]
        top = dices[i][dicematch(botidx)]
        sum += maxside(dices[i], bot)
    maxsum = sum if sum > maxsum else maxsum
print(maxsum)
            
        