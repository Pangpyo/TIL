# 2621 카드게임 S4

colors = []
nums = []

for _ in range(5):
    c, n = input().split()
    colors.append(c)
    nums.append(int(n))

nums.sort()

N = [0] * 10
for i in range(5):
    N[nums[i]] += 1

# 모든 족보에 대해 함수를 만든다

def isflush():
    for i in range(1, 5):
        if colors[i] != colors[i - 1]:
            return False
    return True


def isstraight():
    for i in range(1, 5):
        if nums[i] != nums[i - 1] + 1:
            return False
    return True


def isfourcard():
    if 4 in N:
        return N.index(4)
    else:
        return False


def isfullhouse():
    if 3 in N and 2 in N:
        return (N.index(3), N.index(2))
    else:
        return False


def istriple():
    if 3 in N and 2 not in N:
        return N.index(3)
    else:
        return False


def istwopair():
    if N.count(2) == 2:
        m = []
        for i in range(10):
            if N[i] == 2:
                m.append(i)
        return (max(m), min(m))
    else:
        return False


def ispair():
    if N.count(2) == 1 and 3 not in N:
        return N.index(2)
    else:
        return False


print(N)

M = max(nums)

if isflush() and isstraight():
    print(M + 900)
elif isfourcard():
    print(isfourcard() + 800)
elif isfullhouse():
    a, b = isfullhouse()
    print(700 + a * 10 + b)
elif isflush():
    print(M + 600)
elif isstraight():
    print(M + 500)
elif istriple():
    print(istriple() + 400)
elif istwopair():
    a, b = istwopair()
    print(a * 10 + b + 300)
elif ispair():
    print(ispair() + 200)
else:
    print(M + 100)
