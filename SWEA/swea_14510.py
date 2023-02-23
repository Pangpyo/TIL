import sys


sys.stdin = open("input.txt")

for t in range(1, int(input()) + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    odd = 0
    even = 0
    total = 0
    m = max(trees)
    for tree in trees:
        tr = m - tree
        odd += (m - tree) % 2
        even += (m - tree) // 2
    temp = max(even - odd, 0) // 3
    odd += temp * 2
    even -= temp
    oddEvenMin = min(odd, even)
    ans = (
        oddEvenMin * 2
        + max((odd - oddEvenMin) * 2 - 1, 0)
        + (even - oddEvenMin) // 2 * 3
        + (even - oddEvenMin) % 2 * 2
    )

    print(f"#{t} {ans}")
