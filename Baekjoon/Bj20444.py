# 20444 색종이와 가위 G5

def solution() :
    n, k = map(int, input().split())
    n += 2
    s, e = 1, int(k**0.5) + 1
    while s <= e :
        mid = (s+e)//2
        temp = mid*(n-mid)
        if temp > k :
            e = mid - 1
        elif temp == k :
            return 'YES'
        else :
            s = mid + 1
    return 'NO'

if __name__ == "__main__" :
    print(solution())