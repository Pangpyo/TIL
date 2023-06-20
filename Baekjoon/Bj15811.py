# 15811 복면산 G4

from itertools import permutations


def solution() :
    def trans(c) :
        temp = 0
        for t in c :
            temp *= 10
            temp += dic[t]
        return temp
    a, b, c = map(list, input().split())
    e = sorted(list(set(a + b + c)))
    dic = {}
    
    l = len(e)
    if l > 10 :
        return "NO"
    for per in permutations(range(10), l) :
        for i, n in enumerate(per) :
            dic[e[i]] = n
        if trans(a)+trans(b) == trans(c) :
            return "YES"

    return "NO"

if __name__ == "__main__" :
    print(solution())