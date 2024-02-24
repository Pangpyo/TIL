# 1041 주사위 G5

def solution() :
    N = int(input())
    nums = tuple(map(int, input().split()))
    if N == 1 :
        return sum(nums)-max(nums)
    inf = float('inf')
    level = [inf, inf, inf]
    level[0] = min(nums)
    side = (nums[0], nums[1], nums[5], nums[4])
    for u in (nums[2], nums[3]) :
        for s in range(4) :
            level[1] = min(level[1], u+side[s], side[s]+side[s-1])
            level[2] = min(level[2], u+side[s]+side[s-1])
    use = [0, 0, 0]
    use[2] = 4
    use[1] = (N-1)*8 - 4
    use[0] = N**3 - use[1] - use[2] - (N-2)**2 - (N-2)**3
    answer = use[0]*level[0] + use[1]*level[1] + use[2]*level[2]
    
    return answer

if __name__ == "__main__" :
    print(solution())