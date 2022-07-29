# 11652 카드 S4

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
card = {}
for i in range(n) :
    card_num = int(input())
    if card.get(card_num) :
        card[card_num] += 1
    else :
        card[card_num] = 1

card = sorted(card.items(), key = lambda x: (-x[1], x[0]))

# lambda 를 이용해 key를 카드의 개수의 내림차순, 카드 숫자의 오름차순으로 정렬한다.
print(card[0][0])
