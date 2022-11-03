# 2193 이진수 S3

D = (0, 1)
for i in range(1, int(input())):
    D = (sum(D), D[0])
print(sum(D))
