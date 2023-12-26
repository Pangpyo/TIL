# 5527 전구 장식 G4

def solution() :
    N = int(input())
    L = list(map(int, input().split()))
    D = [1]*N
    answer = 1
    for i in range(1, N) :
        if L[i] != L[i-1] :
            D[i] = D[i-1] + 1
        now = D[i]
        mid = 0
        pre = 0
        if i-now >= 0 :
            mid = D[i-now]
            if i-now-mid >= 0 :
                pre = D[i-now-mid]
        answer = max(answer, now+mid+pre)
    return answer

if __name__ == "__main__" :
    print(solution())