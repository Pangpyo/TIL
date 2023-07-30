# 2302 극장좌석 S1

def solution() :
    N = int(input())
    M = int(input())
    fibo = [0]*41
    fibo[0] = 1
    fibo[1] = 1
    for i in range(2, 41) :
        fibo[i] = fibo[i-1] + fibo[i-2]
    ans = 1
    pre = 1
    P = [int(input()) for _ in range(M)] + [N+1]
    for next in P :
        ans *= fibo[next-pre]
        pre = next+1
    return ans

if __name__ == "__main__" :
    print(solution())
