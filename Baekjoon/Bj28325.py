# 28325 호숫가의 개미굴 G5

def solution() :
    N = int(input())
    nums = tuple(map(int, input().split()))
    D = [[0, 0] for _ in range(N+1)]
    for i in range(1, N) :
        D[i][0] = max(D[i-1]) + nums[i-1]
        D[i][1] = D[i-1][0] + 1
    D[-1][0] = max(D[-2]) + nums[-1]
    answer = max(D[-1])
    D = [[0, 0] for _ in range(N+1)]
    D[1][0] = nums[0]
    for i in range(2, N+1) :
        D[i][0] = max(D[i-1]) + nums[i-1]
        D[i][1] = D[i-1][0] + 1

    answer = max(answer, max(D[-1]))
    return answer

if __name__ == "__main__" :
    print(solution())