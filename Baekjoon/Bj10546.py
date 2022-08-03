# 10546 배부른 마라토너 S4

import sys

sys.stdin = open('input.txt')

N = int(input())
players = {}
for i in range(2*N-1) :
    player = input()
    if player not in players :
        players[player] = 1
    else :
        players[player] += 1

print(*[i for i, v in players.items() if v%2 == 1])