# 22115 창영이와 커피 G5

def solution() :
    N, K = map(int, input().split())
    C = tuple(map(int, input().split()))
    inf = N*2
    D = [inf]*(K+1)
    D[0] = 0
    for c in C :
        for i in reversed(range(1, K+1)) :
            if i >= c :
                D[i] = min(D[i-c] + 1, D[i])
    answer = D[-1]
    return answer if answer != inf else -1

if __name__ == "__main__" :
    print(solution()) 