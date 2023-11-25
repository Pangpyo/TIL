# 카카오 인턴 5

def solution(n, tops):
    answer = 0
    S = [[1, 0] for _ in range(2*n+1)]
    for i in range(n): # 위에 삼각형 있는경우 채우기
        S[1+2*i][1] = tops[i]

    D = [[0, 0] for _ in range(2*n+1)]
    D[0][0] = 1 # [i][0] 채운경우 [i][1] 안채운경우
    D[0][1] = 1
    mod = 10007
    for i in range(1, 2*n+1) :
        D[i][0] = D[i-1][0] + D[i-1][1] # 1개, 가로 2개짜리 채우기
        D[i][1] = D[i-1][0] # 2개짜리 채우기
        if S[i][1] : # 상단 공간이 있는 경우 세로 2개짜리 채우기
            D[i][0] += D[i-1][0]
        D[i][0] %= mod
        D[i][1] %= mod
    answer = D[-1][0]
    return answer




n = 4
tops = [1, 1, 0, 1]
print(solution(n, tops))