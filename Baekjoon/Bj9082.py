# 9082 지뢰찾기 G4

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    for t in range(T):
        N = int(input())
        nums = list(map(int, list(input().rstrip())))
        mine = input().rstrip()
        ans = 0
        for i in range(N):
            if i == 0:
                if nums[0] != 0 and nums[1] != 0:
                    nums[0] -= 1
                    nums[1] -= 1
                    ans += 1
            elif i == (N-1):
                if nums[i] != 0 and nums[i-1] != 0:
                    nums[i-1] -= 1
                    nums[i-2] -= 1
                    ans += 1
            else:
                if nums[i-1] != 0 and nums[i] != 0 and nums[i+1] != 0:
                    nums[i-1] -= 1
                    nums[i] -= 1
                    nums[i+1] -= 1
                    ans += 1
        answer[t] = ans
    return answer
    

if __name__ == "__main__":
    print(*solution(), sep='\n')