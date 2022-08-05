# 15953 상금헌터 B3
# import sys


# sys.stdin = open('input.txt')

first = [5000000] + [3000000]*2 + [2000000]*3 + [500000]*4 + [300000]*5 +[100000]*6
second = []
for i in range(1, 6) :
    second += [10000*(2**(10-i))]*(2**(i-1))

T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    prize1 = first[a-1] if 1 <= a <= 21 else 0
    prize2 = second[b-1] if 1 <= b <= 31 else 0
    print(prize1 + prize2)