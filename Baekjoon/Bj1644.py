# 1644 소수의 연속합 G3


n = int(input())
if n == 1:
    print(0)
else:
    visit = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if visit[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                visit[j] = False

    for i in range(1, len(primes)):
        primes[i] += primes[i - 1]

    primes = [0] + primes
    a = 0
    b = 1
    ans = 0
    while a != b:
        s = primes[b] - primes[a]
        if s <= n:
            b += 1
            if s == n:
                ans += 1
            if b == len(primes):
                break
        else:
            a += 1
    print(ans)
