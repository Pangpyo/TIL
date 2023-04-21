# 1818 책꽂이 G2

from bisect import bisect_left as bl

def solution() :
    N = int(input())
    D = [0]
    for n in map(int, input().split()) :
        if n > D[-1] :
            D.append(n)
        else :
            D[bl(D, n)] = n

    return N-len(D)+1
if __name__ == "__main__" :