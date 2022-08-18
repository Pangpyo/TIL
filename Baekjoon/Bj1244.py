# 1244 스위치 켜고 끄기 S3

import sys


sys.stdin = open('input.txt')

S = int(input())

switch = list(map(int, input().split()))
switch = [-1] + switch
def onoff(a) :
    if switch[a] == 1 :
        switch[a] = 0
    else :
        switch[a] = 1

N = int(input())

for i in range(N) :
    jen, num = map(int, input().split())
    if jen == 1 :
        for j in range(num, S+1, num) :
            onoff(j)
    else :
        r = 0
        for j in range((S+1)//2) :
            if num+j > S or num-j < 1 :
                break
            if switch[num+j] == switch[num-j] :
                r = j
            else :
                break
        for j in range(num-r, num+r+1) :
            onoff(j)
for i in range(1, len(switch)) :
    print(switch[i], end = ' ')
    if i%20 == 0 :
        print()
