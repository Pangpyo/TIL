# 13701 중복 제거

import sys

def solution() :
    input = sys.stdin.readline
    print = sys.stdout.write
    nums = set()
    for n in input().split() :
        if n not in nums :
            print(n)
            print(" ")
            nums.add(n)

if __name__ == "__main__" :
    solution()