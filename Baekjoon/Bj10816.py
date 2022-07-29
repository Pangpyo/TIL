# 10816 숫자카드2 S4

from bisect import bisect, bisect_left, bisect_right
from msilib.schema import Binary
import sys

sys.stdin = open("input.txt")

N = int(input())
card = list(map(int, input().split()))
M = int(input())
card_list = map(int, input().split())
card = sorted(card)

for i in card_list :
    answer = bisect_right(card, i)-bisect_left(card, i)
    print(answer, end = ' ')




# def binary_search(list, n) : # 이분탐색을 위한 함수 정의
#     start = 0
#     last = len(list) - 1
#     while start <= last :
#         mid = (start+last)//2
#         if list[mid] == n : return mid
#         elif list[mid] > n : last = mid - 1
#         else : start = mid + 1
#     return -1

# def binary_left(list, n) : # 이분탐색을 통해 찾은 값에서 가장 왼쪽에 있는 값을 찾는 함수
#     left = binary_search(list, n)
#     while 1 :
#         try :
#             if list[left-1] == n :
#                 left -= 1
#             else : return left
#         except : return left
            
#     return left
        
# def binary_right(list, n) : # 이분탐색을 통해 찾은 값에서 가장 오른쪽에 있는 값을 찾는 함수
#     right = binary_search(list, n)
#     while 1 :
#         try :
#             if list[right+1] == n :
#                 right += 1
#             else : return right
#         except : return right
            
#     return right

# for i in card_list : #
#     if binary_search(card, i) == -1 :
#         print(0, end = ' ')
#     else :
#         answer = binary_right(card, i)-binary_left(card, i)+1
#         print(answer, end = ' ')
    