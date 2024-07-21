# 12841 정보대 등산 S2 


def solution():
    N = int(input())
    cross = tuple(map(int, input().split()))
    left = tuple(map(int, input().split()))
    right = tuple(map(int, input().split()))
    l = 0
    r = cross[0]
    c = 1
    for i in range(1, N):
        l += left[i-1]
        r += right[i-1]
        if l + cross[i] < r:
            c = i + 1
            r = l + cross[i]
    return c, r

if __name__ == "__main__":
    print(*solution())