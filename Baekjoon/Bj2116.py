# 2116 주사위 쌓기 G4

import sys

sys.stdin = open('input.txt')

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

def dicematch(x) : # 주사위의 마주보는 면을 출력해주는 함수
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
    elif x == 5 :
        return 0
maxsum = 0
def maxside(list, botidx) : # 마주보지 않은 4면중 가장 높은 값을 출력해주는 함수
    ans = 0
    topidx = dicematch(botidx)
    for i in range(6) :
        if i not in [botidx, topidx] :
            ans = list[i] if list[i] > ans else ans
    return ans

for j in range(6) :
    sum = 0 # 옆면들의 합을 저장
    bot = dices[0][j] #첫 번째 주사위의 아랫면 결정
    top = dices[0][dicematch(j)] # 첫 번째 주사위의 윗면
    sum += maxside(dices[0], j) # 첫 번째 주사위의 옆 면중 가장 높은 숫자를 sum에 더해줌
    for i in range(1, n) :
        botidx = dices[i].index(top) # 이후 i 번째 주사위들의 아랫면의 인덱스 결정
        bot = dices[i][botidx] # 아랫면의 값
        top = dices[i][dicematch(botidx)] # 윗면의 값
        sum += maxside(dices[i], botidx) # 옆 면중 가장 높은 숫자를 sum에 더해줌
    maxsum = sum if sum > maxsum else maxsum
print(maxsum)
            
        