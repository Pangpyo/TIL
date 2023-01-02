# 20917 사회적 거리 두기 G5


def answer():
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    start = 1
    end = max(x) - min(x)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        pre = x[0]
        cnt = 1
        for i in range(1, n):
            if x[i] - pre >= mid:
                pre = x[i]
                cnt += 1
        if cnt >= s:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


for t in range(int(input())):
    print(answer())
