# 1720 타일 코드 G4

def solution():
    N = int(input())
    D = [0]*(N+1)
    D[0] = 1
    for i in range(1, N+1):
        D[i] += D[i-2]*2 + D[i-1]
    if N % 2:
        sm = D[N//2]
    else:
        sm = D[N//2] + D[N//2 - 1] * 2
    answer = (D[-1]-sm)//2 + sm
    return answer

if __name__ == "__main__":
    print(solution())