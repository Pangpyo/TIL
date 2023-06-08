# 16472 고냥이 G4

from collections import defaultdict

def solution() :
    N = int(input())
    A = list(input())
    have = defaultdict(int)
    temp = 0
    ans = 0
    s = 0
    l = 0
    for e in A :
        if not have[e] :
            l += 1
        have[e] += 1
        temp += 1
        while l > N :
            have[A[s]] -= 1
            temp -= 1
            if not have[A[s]] :
                l -= 1
            s += 1
        ans = max(ans, temp)
    return ans

if __name__ == "__main__" :
    print(solution())