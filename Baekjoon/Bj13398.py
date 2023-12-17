# 13398 연속합 2 G5

def solution() :
    N = int(input())
    A = list(map(int, input().split()))
    D = [[-1000, -1000] for _ in range(N)]
    for i in range(N) :
        D[i][0] = max(D[i-1][0] + A[i], A[i])
        D[i][1] = max(D[i-1][1] + A[i], D[i-1][0])
    answer = max(map(max, D))
    return answer

if __name__ == "__main__" :
    print(solution())