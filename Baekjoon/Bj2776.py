# 2776 암기왕 S4
import sys

sys.stdin = open('input.txt')

T = int(input())

def binary_search(list, n) : # 시간 초과가 나지 않도록 이진탐색을 활용했다.
    start = 0
    last = len(list) - 1
    while start <= last :
        mid = (start+last)//2
        if list[mid] == n : return mid
        elif list[mid] > n : last = mid - 1
        else : start = mid + 1
    return -1

for _ in range(T) :
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    for i in note2 :
        if binary_search(note1, i) == -1 :
            print(0)
        else :
            print(1)

