# 17828 문자열 화폐 G5

import sys


def solution() :
    print = sys.stdout.write
    N, X = map(int, input().split())
    if X < N :
        print('!')
        return
    X -= N
    Z = X//25
    M = X%25
    cnt = Z + int(M!=0)
    if cnt > N :
        print('!')
        return
    print('A'*(N-cnt))
    if M :
        print(chr(ord('A')+M))
    print('Z'*Z)

if __name__ == "__main__" :
    solution()