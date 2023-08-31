# 17251 힘 겨루기 G5

def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    mv, idx = 0, 0
    for i, v in enumerate(nums) :
       if mv <= v :
           mv = v
           idx = i 
    rmv = 0
    win = [0, 0, 0]
    for i in range(N-1) :
        v = nums[i]
        rmv = max(v, rmv)
        if rmv == mv :
            if i < idx :
                win[1] += 1
            else :
                win[0] += 1
        else :
            win[2] += 1

    if win[0] > win[2] :
        return 'R'
    elif win[0] < win[2] :
        return 'B'
    else :
        return 'X'

if __name__ == "__main__" :
    print(solution())