# 2022 카카오 기출

def solution(board, skills):
    N = len(board)
    M = len(board[0])
    nsum = [[0]*(M+1) for _ in range(N+1)]
    for skill in skills :
        t, r1, c1, r2, c2, d = skill # 시간 복잡도를 줄이려면 누적합을 사용해야한다.
        d = -d if t ==1 else d
        nsum[r1][c1] += d
        nsum[r1][c2+1] += -d
        nsum[r2+1][c1] += -d
        nsum[r2+1][c2+1] += d

    for i in range(N+1) :
        for j in range(1, M+1) :
            nsum[i][j] += nsum[i][j-1]
    for j in range(M+1) :
        for i in range(1, N+1) :
            nsum[i][j] += nsum[i-1][j]

    answer = 0
    for i in range(N) :
        for j in range(M) :
            ans = board[i][j] + nsum[i][j]
            if ans > 0 :
                answer += 1
    
    return answer