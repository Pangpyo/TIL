# 1. 1936 1대1 가위바위보 D1

A, B = map(int, input().split())

def RSP(a, b) :
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) :
        return 'A'
    else :
        return 'B'

print(RSP(A,B))
    