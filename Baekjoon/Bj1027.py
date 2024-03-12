# 1027 고층 건물 G4

from fractions import Fraction


def solution() :
    N = int(input())
    B = tuple(map(int, input().split()))
    def see(m, d) :
        b = B[m]
        s = m + d
        maxh = -float('inf')
        cnt = 0
        while s >= 0 and s < N :
            h = Fraction((B[s] - b), abs(m-s))
            if h > maxh :
                maxh = h
                cnt += 1
            s += d
        return cnt
    answer = 0
    for i in range(N) :
        answer = max(answer, see(i, -1) + see(i, +1))
    return answer

if __name__ == "__main__" :
    print(solution())