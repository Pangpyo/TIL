# 2938 3으로 나누어 떨어지지 않는 배열 G5

def solution():
    N = int(input())
    nums = [[], [], []]
    for num in map(int, input().split()):
        nums[num % 3].append(num)
    if len(nums[0]) > (N+1)//2 or (len(nums[0]) == 0 and len(nums[1]) > 0 and len(nums[2]) > 1):
        return [-1]
    answer = []
    while nums[1]:
        if len(nums[0]) > 1:
            answer.append(nums[0].pop())
        answer.append(nums[1].pop())
    if nums[0]:
        answer.append(nums[0].pop())
    while nums[2]:
        answer.append(nums[2].pop())
        if nums[0]:
            answer.append(nums[0].pop())
    return answer

if __name__ == "__main__":
    print(*solution())