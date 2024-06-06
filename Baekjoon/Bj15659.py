# 15659 연산자 끼워넣기 (3) G4

def solution():
    N = int(input())
    nums = [""]*(N * 2 - 1)
    for i, n in enumerate(input().split()):
        nums[i*2] = n
    INF = float('inf')
    answer = [-INF, INF]
    cnts = list(map(int, input().split()))
    exps = ["+", "-", "*", "//"]
    def permu(n):
        if n == N - 1:
            val = eval(''.join(nums))
            answer[0] = max(val, answer[0])
            answer[1] = min(val, answer[1])
        for i in range(4):
            if cnts[i]:
                cnts[i] -= 1
                nums[n*2+1] = exps[i]
                permu(n+1)
                cnts[i] += 1
    permu(0)
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')