# 1301 비즈 공예 G3

def solution() :
    N = int(input())
    bizz = [0]*5
    for i in range(N) :
        bizz[i] = int(input())
    dp = [[[[[[[-1]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(6)] for _ in range(6)]

    def make_bizz(pp, p, a, b, c, d, e) :
        if ((pp != 0 and p != 0) and pp == p) or (a < 0 or b < 0 or c < 0 or d < 0 or e < 0) :
            return 0
        if (a, b, c, d, e) == (0, 0, 0, 0, 0) :
            return 1
        temp = dp[pp][p][a][b][c][d][e]
        if temp != -1 :
            return temp
        temp = 0
        if a > 0 and pp != 1 and p != 1 :
            temp += make_bizz(p, 1, a-1, b, c, d, e)
        if b > 0 and pp != 2 and p != 2 :
            temp += make_bizz(p, 2, a, b-1, c, d, e)
        if c > 0 and pp != 3 and p != 3 :
            temp += make_bizz(p, 3, a, b, c-1, d, e)
        if d > 0 and pp != 4 and p != 4 :
            temp += make_bizz(p, 4, a, b, c, d-1, e)
        if e > 0 and pp != 5 and p != 5 :
            temp += make_bizz(p, 5, a, b, c, d, e-1)
        dp[pp][p][a][b][c][d][e] = temp
        return temp
    answer = make_bizz(0, 0, *bizz)
    return answer

if __name__ == "__main__" :
    print(solution())