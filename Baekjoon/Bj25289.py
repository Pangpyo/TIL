# 25289 가장 긴 등차 부분 수열 G4

def solution():
    N = int(input())
    nums = tuple(map(int, input().split()))
    answer = 0
    MAX = 100
    for d in range(-99, 100):
        dp = [0]*(MAX+1)
        for n in nums:
            if 0 < n - d <= MAX:
                dp[n] = max(dp[n], dp[n-d] + 1)
            else:
                dp[n] = 1
        answer = max(answer, max(dp))
    return answer

if __name__ == "__main__":
    print(solution())