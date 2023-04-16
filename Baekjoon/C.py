# C 고양이는 많을수록 좋다

N = int(input())
if N:
    a = 1
    cnt = 1
    while a < N:
        a <<= 1
        cnt += 1
    print(cnt)
else:
    print(0)
