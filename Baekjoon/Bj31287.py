# 31287 장난감 강아지 S2

def solution():
    N, K = map(int, input().split())
    S = input()
    x, y = 0, 0
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    dr = {"U":0, "R":1, "D":2, "L":3}
    MAX = 5_000_000
    for i in range(min(N*K, MAX)):
        d = dr[S[i%N]]
        x += dx[d]
        y += dy[d]
        if (x, y) == (0, 0):
            return "YES"
    return "NO"

if __name__ == "__main__":
    print(solution())