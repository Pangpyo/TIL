# 25304 영수증 B5

X = int(input())
N = int(input())
total = 0
for i in range(N) :
    a, b = map(int, input().split())
    total += a*b
print('Yes' if total == X else 'No')