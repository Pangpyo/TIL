# 24023 아기 홍윤 G5

def solution() :
    N, K = map(int, input().split())
    MAX = 30
    bit = [0]*(MAX+1)
    nums = tuple(map(int, input().split()))
    s, e = 0, 0
    for n in nums :
        e += 1
        for i in range(MAX+1) :
            if n & (1<<i) :
                bit[i] += 1
        while True :
            temp = 0
            for i in range(MAX+1) :
                if bit[i] :
                    temp += (1<<i)
            if temp == K :
                return [s+1, e]
            elif temp < K :
                break
            for i in range(MAX+1) :
                if nums[s] & (1<<i) :
                    bit[i] -= 1
            s += 1
    return [-1]

if __name__ == "__main__" :
    print(*solution())