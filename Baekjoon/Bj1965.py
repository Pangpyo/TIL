# 1965 상자넣기 S2

from bisect import bisect_left


def solution():
    N = int(input())
    dp = [0]
    for box in map(int, input().split()):
        if box > dp[-1]:
            dp.append(box)
        elif box < dp[-1]:
            dp[bisect_left(dp, box)] = box
    
    return len(dp) - 1

if __name__ == "__main__":
    print(solution())