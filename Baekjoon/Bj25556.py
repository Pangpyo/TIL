# 25556 포스택 G5

def solution() :
    N = int(input())
    A = tuple(map(int, input().split()))
    visit = [0]*N
    for _ in range(4) :
        pre = 0
        for i, n in enumerate(A) :
            if visit[i] :
                continue
            if pre < n :
                pre = n
                visit[i] = 1
    if sum(visit) == N :
        return "YES"
    return "NO"

if __name__ == "__main__" :
    print(solution())