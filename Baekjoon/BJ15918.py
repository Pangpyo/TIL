# 15918 랭퍼든 수열쟁이야!! G5

def solution() :
    ans = 0
    n, x, y = map(int, input().split())
    x, y = x-1, y-1
    rpd_arr = [0]*(2*n)
    used = [0]*(n+1)
    def rpd(idx) :
        nonlocal ans
        if rpd_arr[x] and rpd_arr[y] and rpd_arr[x] != rpd_arr[y]:
             return 
        if idx == 2*n :
            ans += 1
            return
        if rpd_arr[idx] :
            rpd(idx+1)
        for i in range(1, n+1) :
            if used[i] :
                continue
            if idx+1+i >= 2*n or rpd_arr[idx] or rpd_arr[idx+1+i] :
                continue
            used[i] = 1
            rpd_arr[idx] = i
            rpd_arr[idx+i+1] = i
            rpd(idx+1)
            used[i] = 0
            rpd_arr[idx] = 0
            rpd_arr[idx+i+1] = 0
    rpd(0)
    return ans

if __name__ == "__main__" :
    print(solution())

