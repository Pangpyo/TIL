# 14225 부분수열의 합 S1

def solution():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    MAX = 100_000
    visit = [0]*(N*MAX + 1)
    def comb(a, n):
        if n == N:
            return
        for i in range(n, N):
            na = a + S[i]
            visit[na] = 1
            comb(na, i+1)
    comb(0, 0)
    answer = 1
    for i in range(1, N*MAX + 1):
        if not visit[i]:
            answer = i
            break
    return answer

if __name__ == "__main__":
    print(solution())