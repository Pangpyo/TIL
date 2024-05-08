# 25194 결전의 금요일 G5

def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    days = [0]*7
    for i in range(N):
        nums[i] %= 7
    for i in range(N):
        n = nums[i]
        temp = [0]*7
        for k in range(7):
           if days[k]:
                temp[(n+k)%7] = 1
        for j in range(7):
            if temp[j]:
                days[j] = 1
        days[n] = 1
    answer = "YES" if days[4] else "NO"
    return answer

if __name__ == "__main__":
    print(solution())