# 20159 동작 그만, 밑장 빼기냐? G4

def soltion() :
    N = int(input())
    nums = list(map(int, input().split()))
    even_sum = [0]
    odd_sum = [0]
    for i in range(0, N, 2) :
        even_sum.append(even_sum[-1]+nums[i])
        odd_sum.append(odd_sum[-1]+nums[i+1])
    answer = max(even_sum[-1], odd_sum[-1])
    for i in range(1, N//2+1) :
        answer = max(answer, even_sum[i]-odd_sum[i-1]+odd_sum[-2], odd_sum[-1]-odd_sum[i]+even_sum[i])
    return answer

if __name__ == "__main__" :
    print(soltion())