# 2036 수열의 점수 G4

import sys


def solution() :
    input = sys.stdin.readline
    n = int(input())
    m = []
    one = []
    p = []
    for i in range(n) :
        a = int(input())
        if a <= 0 :
            m.append(a)
        elif a == 1 :
            one.append(a)
        else :
            p.append(a)
    m.sort(reverse=True)
    p.sort()
    ans = 0
    def score(arr) :
        ans = 0
        while arr :
            a = arr.pop()
            if not arr :
                ans += a
                break
            b = arr.pop()
            ans += a*b
        return ans
    
    ans = score(m) + score(p) + sum(one)
    return ans

if __name__ == "__main__" :
    print(solution())