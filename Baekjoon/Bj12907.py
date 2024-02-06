# 12907 동물원 G5

def solution() :
    N = int(input())
    nums = [0]*(N+2)
    nums[-1] = 2
    for n in map(int, input().split()) :
        if n > N :
            return 0
        nums[n] += 1
        if nums[n] > 2 :
            return 0
    answer = 1
    for i in range(N+1) :
        if nums[i] > nums[i-1] :
            return 0
        if nums[i] == 0 :
            continue
        if nums[i-1] == 2 :
            answer *= 2
    return answer

if __name__ == "__main__" :
    print(solution())