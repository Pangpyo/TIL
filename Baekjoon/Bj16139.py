# 16139 인간-컴퓨터 상호작용 S1


import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
S = input()
Slist = [[0]*26 for _ in range(len(S))]
for i in range(1, len(S)) :
    for j in range(26) :
        if ord(S[i-1])-97==j:
            Slist[i][j] = Slist[i-1][j] + 1
        else :
            Slist[i][j] = Slist[i-1][j]
for _ in range(int(input())) :
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    ans = Slist[r+1][ord(a)-97]-Slist[l][ord(a)-97]
    sys.stdout.write(str(ans)+'\n')

# import sys


# sys.stdin = open('input.txt')
# input = sys.stdin.readline
# S = input()

# q = int(input())


# for _ in range(q) :
#     a, l, r = input().split()
#     l = int(l)
#     r = int(r)
#     lis = [0]*(len(S)+1)
#     for i in range(len(S)) :
#         lis[i+1] = lis[i]
#         if S[i] == a :
#             lis[i+1] = lis[i] +1
#     ans = lis[r+1]-lis[l]
#     sys.stdout.write(str(ans)+'\n')
# 50점에서 그쳤다. 다음에 다시 도전해야겠다.

