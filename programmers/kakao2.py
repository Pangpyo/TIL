from bisect import bisect_right

def solution(cap, n, deliveries, pickups):
    dsum = [0]
    psum = [0]
    for i in range(n-1, -1 ,-1) :
        dsum.append(dsum[-1] + deliveries[i])
        psum.append(psum[-1] + pickups[i])
    dsum = dsum[1::]
    psum = psum[1::]
    deli = 0
    pick = 0
    for i in range(n-1, -1, -1) :
        if deliveries[i] :
            deli = i+1
            break
    for i in range(n-1, -1, -1) :
        if pickups[i] :
            pick = i+1
            break
    cnt = 0
    ans = 0
    while 1 :
        cnt += cap
        des = max(deli, pick)
        deli = n - bisect_right(dsum, cnt)
        pick = n - bisect_right(psum, cnt)
        ans += des*2

        if not deli and not pick :
            break

    return ans
