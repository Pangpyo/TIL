# 16288 Passport Control G3

def solution():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = N
    visit = [0] * N
    need = 0
    while cnt:
        pre = 0
        for i in range(N):
            if visit[i]:
                continue
            if pre < nums[i]:
                pre = nums[i]
                visit[i] = 1
                cnt -= 1
        need += 1
    if need <= K:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    print(solution())