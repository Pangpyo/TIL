# 16766 Convention G4

def solution() :
    N, M, C = map(int, input().split())
    cows = list(map(int, input().split()))
    cows.sort()
    s, e = 0, max(cows)
    answer = float('inf')
    while s <= e :
        m = (s+e)//2
        bus = 1
        cnt = 0
        pre = cows[0]
        for cow in cows :
            if cnt == C or cow - pre > m:
                bus += 1
                cnt = 0
                pre = cow
            cnt += 1
        if bus <= M :
            answer = min(m, answer)
            e = m - 1
        else :
            s = m + 1
    return answer

if __name__ == "__main__" :
    print(solution())