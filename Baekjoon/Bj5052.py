# 5052 전화번호 목록 G4

import sys


def solution():
    input = sys.stdin.readline

    numbers = []
    K = int(input())
    for i in range(K):
        numbers.append(input().rstrip())
    numbers = sorted(numbers)
    head = "*"
    for n in numbers:
        if head == n[0 : len(head)]:
            return "NO"
        else:
            head = n
    return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())
