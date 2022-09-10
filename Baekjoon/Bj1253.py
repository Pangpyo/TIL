# 1253 좋다 G4

import sys


sys.stdin = open('input.txt')

N = int(input())

nums = list(map(int, input().split()))

nums.sort()

def binary_search(list, n, i, j) : # 이분탐색을 위한 함수 정의
    start = 0
    last = len(list) - 1
    while start <= last :
        mid = (start+last)//2
        if list[mid] == n : 
            if mid == i :
                if mid + 1 < N and list[mid+1] == n and mid+1 != j:
                    return mid + 1
                elif mid -1 >= 0 and list[mid-1] == n and mid+1 != j:
                    return mid - 1
                return -1
            if mid == j :
                if mid + 1 < N and list[mid+1] == n and mid+1 != i:
                    return mid + 1
                elif mid -1 >= 0 and list[mid-1] == n and mid+1 != i:
                    return mid - 1
                return -1   
            else :
                return mid
        elif list[mid] > n : last = mid - 1
        else : start = mid + 1
    return -1
ans = 0
for i in range(N) :
    for j in range(N) :
        if i == j:
            continue
        if binary_search(nums, nums[i]-nums[j], i, j) != -1 :
            ans += 1
            print(nums[i], nums[j], nums[binary_search(nums, nums[i]-nums[j], i,j)])
            break
print(ans)