# 2195 문자열 복사 G5

def solution() :
    S = input()
    P = input()
    S += '.'
    target = len(P)
    n = 0
    answer = 0
    while n < target:
        answer += 1
        a = 0
        cnt = 0
        for s in S :
            if n+a == target :
                cnt = a
                break
            if s == P[n+a] :
                a += 1
            else :
                cnt = max(cnt, a)
                a = 0
        n += cnt
    return answer

if __name__ == "__main__" :
    print(solution())