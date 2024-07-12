# 27277 장기자랑 S1

def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.append(0)
    nums.sort()
    answer = 0
    s, e = 0, N
    while s < e:
        answer += nums[e] - nums[s]
        s += 1
        e -= 1
    return answer

if __name__ == "__main__":
    print(solution())

