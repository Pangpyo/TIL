# 7570 줄세우기


def solution():
    N = int(input())
    nums = [0] * N
    for i, n in enumerate(map(int, input().split())):
        nums[n - 1] = i
    temp = 1
    ans = 1
    for i in range(1, N):
        if nums[i] > nums[i - 1]:
            temp += 1
        else:
            temp = 1
        ans = max(ans, temp)
    return N - ans


if __name__ == "__main__":
    print(solution())
