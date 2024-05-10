# 12886 돌 그룹 G4

from collections import deque


def solution():
    nums = list(map(int, input().split()))
    que = deque()
    nums.sort()
    nums = tuple(nums)
    que.append(nums)
    def plus(a, b):
        if a < b:
            return a*2
        else:
            return a-b
    visit = set()
    visit.add(nums)
    if nums[0] == nums[1] == nums[2]:
        return 1
    while que:
        nums = que.popleft()
        for i in range(2):
            for j in range(i+1, 3):
                if nums[i] == nums[j]:
                    continue
                nnums = list(nums)
                nnums[i] = plus(nums[i], nums[j])
                nnums[j] = plus(nums[j], nums[i])
                nnums.sort()
                nnums = tuple(nnums)
                if nnums[0] == nnums[1] == nnums[2]:
                    return 1
                if nnums in visit:
                    continue
                visit.add(nnums)
                que.append(nnums)
                
    return 0

if __name__ == "__main__":
    print(solution())