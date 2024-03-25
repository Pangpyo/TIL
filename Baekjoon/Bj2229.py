# 2229 조 짜기 G5

def solution() :
    N = int(input())
    scores = tuple(map(int, input().split()))
    D = [0]*(N+1)
    INF = 10001
    for i in range(1, N) :
        for j in range(i) :
            max_ = -1
            min_ = INF
            for k in range(i-j-1, i+1) :
                max_ = max(max_, scores[k])
                min_ = min(min_, scores[k])
            D[i] = max(D[i], D[i-j-2] + abs(max_ - min_))
    return D[-2]

if __name__ == "__main__" :
    print(solution())