# 23560 약 S2

from collections import defaultdict


def solution():
    N = int(input())
    medicine_bags = "010"*N
    dp = defaultdict(int)
    dp[""] = 1
    dp["1"] = 1
    dp["10"] = 1
    dp["01"] = 1
    def take_medicine(medicine_bags, eat):
        if dp[medicine_bags] != 0:
            return dp[medicine_bags]
        temp = 0
        need = "1" if eat%3 == 1 else "0"
        if medicine_bags[0] == need:
            temp += take_medicine(medicine_bags[1::], eat + 1)
        if medicine_bags[-1] == need:
            temp += take_medicine(medicine_bags[0:-1], eat + 1)
        dp[medicine_bags] = temp
        return temp
    answer = take_medicine(medicine_bags, 0)
    return answer

if __name__ == "__main__":
    print(solution())