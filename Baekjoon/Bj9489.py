# 9489 사촌 G4

import sys


def solution():
    input = sys.stdin.readline
    answers = []
    while True:
        n,k = map(int,input().rstrip().split())
        if n==0 and k == 0:
            break
        a = (-1,) + tuple(map(int,input().rstrip().split()))
        parent = [0]*(n+1)
        parent[0] = -1
        target = 0
        idx = -1
        for i in range(1,n+1):
            if a[i] == k:
                target = i
            if a[i] != a[i-1]+1:
                idx+=1
            parent[i] = idx
        answer = 0
        for i in range(1,n+1):
            if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
                answer+=1
        answers.append(answer)
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')