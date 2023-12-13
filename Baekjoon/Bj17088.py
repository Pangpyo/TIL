# 17088 등차수열 변환 G5

def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    inf = float('inf')
    if N == 1 :
        return 0
    min_diff = inf
    max_diff = -inf
    for i in range(1, N) :
        diff = nums[i] - nums[i-1]
        min_diff = min(diff, min_diff)
        max_diff = max(diff, max_diff)
    if abs(min_diff-max_diff) > 5 :
        return -1

    answer = inf
    for diff in range(min_diff, max_diff+1) :
        for n in (-1, 0, 1) :
            pre = nums[0] + n
            cnt = abs(n)
            flag = True
            for i in range(1, N) :
                d = nums[i] - pre
                if d == diff :
                    pre = nums[i]
                elif d == diff - 1 :
                    pre = nums[i] + 1
                    cnt += 1
                elif d == diff + 1 :
                    pre = nums[i] - 1
                    cnt += 1
                else :
                    flag = False
                    break
            if flag :
                answer = min(answer, cnt)
    if answer == inf:
        return -1
    return answer

if __name__ == "__main__" :
    print(solution())