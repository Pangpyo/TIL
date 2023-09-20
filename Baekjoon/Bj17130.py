# 17130 토끼가 정보섬에 올라온 이유 G4
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = []
    sx, sy = 0, 0
    for i in range(N) :
        temp = tuple(input().rstrip())
        for j in range(M) :
            if temp[j] == 'R' :
                sx, sy = i, j
        P.append(temp)
    answer = -1
    D = [[-1]*M for _ in range(N)]
    D[sx][sy] = 0
    for j in range(M-1) :
        for i in range(N) :
            if D[i][j] == -1 :
                continue
            for k in (-1, 0, 1) :
                ni = i + k
                if ni >= N or ni < 0 or P[ni][j+1] == '#':
                    continue

                D[ni][j+1] = max(D[ni][j+1], D[i][j] + int(P[ni][j+1] == 'C'))
                if P[ni][j+1] == 'O' :
                    answer = max(answer, D[ni][j+1])
    return answer
    

if __name__ == "__main__" :
    print(solution())
