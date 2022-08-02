# 23253 자료구조는 정말 최고야 S5


import sys
sys.stdin = open('18_자료구조는.txt')
input = sys.stdin.readline # 여러줄 입력 받으므로 입력시간을 줄이기 위해 사용
N, M = map(int, input().split()) # N, M을 정수형으로 입력받음

for i in range(M) : 
    l = int(input()) 
    books = list(map(int, input().split()))
    for j in range(l-1) : 
        if books[j] < books[j+1] : 
# 쌓인 더미가 큰 수부터 나와야만 책을 순서대로 꺼낼 수 있다.
            print('No')
            exit(0) # if문이 실행 될 경우 프로그램 종료
print('Yes') # if문이 실행되지 않을 경우 'Yes' 출력