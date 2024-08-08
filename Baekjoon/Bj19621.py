# 19621 회의실 배정 2

def solution():
    N = int(input())
    tasks = tuple(tuple(map(int, input().split())) for _ in range(N))
    D = [0]*(N+1)
    for i in range(1, N+1):
        D[i] = max(D[i-1], D[i-2]+tasks[i-1][2])
    
    return D[-1]

if __name__ == "__main__":
    print(solution())