# 29155 개발자 지망생 구름이의 취업 뽀개기

def solution() :
    N = int(input())
    p = list(map(int, input().split()))
    probs = [tuple(map(int, input().split())) for _ in range(N)]
    probs.sort()
    ans = 0
    prel, pret = 0, 0
    for l, t in probs :
        if not p[l-1] :
            continue
        if prel :
            if prel == l :
                ans += t-pret
            else :
                ans += 60
        ans += t
        prel = l
        pret = t
        p[l-1] -= 1
    return ans

if __name__ == "__main__" :
    print(solution())