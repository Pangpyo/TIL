# 16496 큰 수 만들기 P5

N = int(input())
nums = sorted(
    list(input().split()),
    reverse=True,
    key=lambda x: (x * (10 // len(x) + 2))[:11],
)
print(int("".join(nums)))
