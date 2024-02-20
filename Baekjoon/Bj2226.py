# 2226 이진수 G4

def solution() :
    N = int(input())
    if N == 1 :
        return 0
    elif N <= 3 :
        return 1
    a = (0, 0, 1)
    b = (1, 0, 0)
    def connect(a, b) :
        mid = a[1]+b[1]
        if a[2] or b[0] :
            mid += 1
        return (a[0], mid, b[2])
    for _ in range(3, N) :
        na = connect(b, a)
        nb = connect(a, b)
        a = na
        b = nb

    return sum(connect(a, b))

if __name__ == "__main__" :
    print(solution())