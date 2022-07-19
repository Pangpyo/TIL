import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def zot(a) : 
    if a == '0' :
        b = '1'
    elif a == '1' :
        b = '0'
    else : b = a
    return b

for i in range(1,T+1) :
    S = input()
    N = len(S)
    for i in range(10) :
        if S[1] == '1' :
            S[1] = '2'
            S[j+1] = str(zot(S[j+1]))
        for j in range(1,N) :
            if S[j] == '1' :
                S[j] = '2'
                S[j-1] = str(zot(S[j-1]))
                S[j+1] = str(zot(S[j+1]))
        if S[N] == '1' :
            S[j] = '2'
            S[j-1] = str(zot(S[j-1]))