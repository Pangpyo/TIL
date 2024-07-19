# 20117 호반우 상인의 이상한 품질 계산법 S1

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s, e = 0, N-1
    answer = 0
    while s < e:
        answer += A[e]*2
        s += 1
        e -= 1
    if N % 2:
        answer += A[N//2]
    return answer

if __name__ == "__main__":
    print(solution())