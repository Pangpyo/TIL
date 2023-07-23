# 16193 차이를 최대로 2 G2

def solution() :
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    def sol(half) :
        if not N%2 :
            ans = sum(half[0])*2 - half[0][0] - (sum(half[1])*2 - half[1][-1])
        else :
            half[0].reverse()
            arr = [0]*N
            arr[0] = half[0][0]
            ans = 0
            small = float('inf')
            for i in range(1, N) :
                arr[i] = half[i%2][i//2]
                diff = abs(arr[i]-arr[i-1])
                ans += diff
                small = min(small, diff)
            ans += abs(arr[-1]-arr[0])
            small = min(small, abs(arr[-1]-arr[0]))
            ans -= small
        return ans
    H = N//2
    half = [A[H:N], A[0:H]]
    ans = sol(half)
    H = (N+1)//2
    half = [A[0:H], A[H:N]]
    ans = max(ans, sol(half))
    return ans

if __name__ == "__main__" :
    print(solution())