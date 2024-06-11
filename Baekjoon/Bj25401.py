# 25401 카드 바꾸기 G5

def solution():
    N = int(input())
    nums = tuple(map(int, input().split()))
    answer = float('inf')
    for i, n in enumerate(nums):
        for j in range(i+1, N):
            nn = nums[j]
            if (nn - n) % (j - i):
                continue
            diff = (nn - n) // (j - i)
            temp = 0
            for k, nnn in enumerate(nums):
                if nnn != n + diff * (k - i):
                    temp += 1
            answer = min(temp, answer)
    return answer

if __name__ == "__main__":
    print(solution())