# 11286 절댓값 힙 S1

import heapq
import sys

sys.stdin = open('21_절댓값힙.txt')

input = sys.stdin.readline 
heap = [] 
N = int(input()) 

for i in range(N) :
    x = int(input())
    if x == 0 : #x가 0일 경우 실행한다.
        if len(heap) == 0 : # heap에 인덱스가 없을 경우 0을 출력한다
            print(0)
        else :
            print(heapq.heappop(heap)[1])  
# heappop 메서드를 이용해 가장 앞에있는 튜플을 제거하며 그 1번째 인덱스, 즉 절댓값을 하기 전의 값을 출력한다.
    else :
        heapq.heappush(heap, (abs(x),x)) 
# (x의 절댓값, x) 순으로 푸쉬하면 절댓값 크기순, x크기순의 오름차순으로 정렬된다.
