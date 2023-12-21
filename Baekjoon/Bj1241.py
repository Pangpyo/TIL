# 1241 머리 톡톡 G5

def solution() :
    N = int(input())
    MAX = 1_000_000
    nums = [0]*(MAX+1)
    student = [0]*N
    cnts = [0]*(MAX+1)
    for i in range(N) :
        n = int(input())
        nums[n] += 1
        cnts[n] += 1
        student[i] = n
        
    for i in range(1, MAX//2+1) :
        for j in range(i+i, MAX+1, i) :
            cnts[j] += nums[i]
    answer = [0]*N
    for i in range(N) :
        answer[i] = cnts[student[i]]-1
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')