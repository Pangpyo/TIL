# 14852 타일 채우기 3 G4

def solution() :
    N = int(input())
    d1 = 1
    d2 = 0
    d3 = 0
    dd1 = 0
    dd = 0
    MOD = 1_000_000_007
    for i in range(N) :
        if i == 3 :
            dd1 = 1
        dd = (dd1 + d3) % MOD
        d = (d1 * 2 + d2 * 3 + dd * 2) % MOD
        dd1 = dd
        d3 = d2
        d2 = d1
        d1 = d
    return d


if __name__ == "__main__" :
    print(solution())