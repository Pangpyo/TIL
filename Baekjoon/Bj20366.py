# 20366 같이 눈사람 만들래? G3

def solution() :
    N = int(input())
    snows = list(map(int, input().split()))
    S = []
    for i in range(N) :
        for j in range(i+1, N) :
            S.append((snows[i]+snows[j], i, j))
    S.sort()
    M = len(S)
    s, e = 0, 1
    ans = float('inf')
    while True :
        if s == e :
            if s == M-1 :
                break
            e += 1
        pre, a, b = S[s]
        now, c, d = S[e]
        flag = a != c and a != d and b != c and b != d
        if flag :
            ans = min(ans, now-pre)
        s += 1
    return ans

if __name__ == "__main__" :
    print(solution())