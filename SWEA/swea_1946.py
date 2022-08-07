# 1946 간단한 압축 풀기 D2

import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    word = '' # 압축을 푼 문자열을 열렬로 받아줌
    for _ in range(N) :
        c, i = input().split()
        word += c*int(i)
    print('#%d'%t)
    while word : # 일렬로 압축이 풀린 문자열들을 10개씩 출력
        print(word[0:10])
        word = word[10::]
