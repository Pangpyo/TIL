# 23742 player-based Team G4

def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    cnt = 0
    sums = 0
    
    for n in nums :
        if (cnt+1)*n + sums >= n :
            cnt += 1
            sums += n
        else :
            break
    answer = cnt*sums + sum(nums[cnt::])
    return answer

if __name__ == "__main__" :
    print(solution())