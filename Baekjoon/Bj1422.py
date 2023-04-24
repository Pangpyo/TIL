# 1422 숫자의 신 P4

def solution() :
    K, N = map(int, input().split())
    nums = [input() for _ in range(K)]
    for _ in range(N-K) :
        nums.append(str(max(map(int, nums)))) 
    nums.sort(reverse=True, key=lambda x : ((x*10)[0:10]))
    print(*nums, sep="")

if __name__ == "__main__" :
    solution()