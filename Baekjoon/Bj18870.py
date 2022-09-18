# 18870 좌표압축 S2

from bisect import bisect
import sys

input = sys.stdin.readline # 표준입력 사용

N = int(input()) 
nums = list(map(int, input().split())) 
snums = sorted(list(set(nums))) #중복을 제거해주고, 크기 순으로 정렬해줌
znums = []
for i in range(N) :
    znums.append(bisect(snums, nums[i])-1) # 내가 찾고자 하는 수가 몇 번째 인덱스에 있는지 이분탐색을 통해 찾아줌
print(*znums)