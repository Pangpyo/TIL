# 16209 수열 섞기 G3


def solution() :
    N = int(input())
    minus = []
    plus = []
    for n in map(int, input().split()) :
        if n <= 0 :
            minus.append(n)
        else :
            plus.append(n)
    minus.sort(reverse=True)
    plus.sort()

    answer = []
    def make_array(nums) :
        l = []
        r = []
        for i, n in enumerate(nums) :
            if i%2 :
                l.append(n)
            else :
                r.append(n)
        r.reverse()
        return l+r
    answer = make_array(minus) + make_array(plus)[::-1]

    return answer

if __name__ == "__main__" :
    print(*solution())