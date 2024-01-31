# 3013 부분 수열의 중앙값 G3

def solution() :
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    D = [0]*N
    cnt = [0]*(N+1)
    flag = True
    point = 0
    for i, a in enumerate(A) :
        D[i] += D[i-1]
        if a < B :
            D[i] -= 1
        elif a > B :
            D[i] += 1
        if a == B :
            flag = False
            point = i
        if flag :
            cnt[D[i]] += 1
    answer = 0
    for i in range(point, N) :
        if D[i] == 0 :
            answer += 1
        answer += cnt[D[i]]
    return answer

if __name__ == "__main__" :
    print(solution())