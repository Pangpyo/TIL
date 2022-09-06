# 5052 전화번호 목록 G4

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline



for _ in range(int(input())) :
    numbers = []
    ans = 'YES'
    K = int(input())
    for i in range(K) :
        numbers.append(input().rstrip())
    numbers = sorted(numbers)
    head = '*'
    for n in numbers :
        if head == n[0:len(head)] :
            ans = 'NO'
            break
        else :
            head = n
    print(ans)