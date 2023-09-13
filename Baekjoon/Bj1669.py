# 1669 멍멍이 쓰다듬기 G5

def solution() :
    X, Y = map(int, input().split())
    diff = Y-X
    sqr = int(diff**0.5)
    if not diff :
        return 0
    cnt = sqr*2 - 1
    diff -= sqr*sqr
    while diff and sqr >= 1:
        if sqr <= diff :
            cnt += diff//sqr
            diff %= sqr
        sqr -= 1
    return cnt

if __name__ == "__main__" :
    print(solution())

