# 25635 자유 이용권 G4


def solution() :
    input()
    A = list(map(int, input().split()))
    max_A = max(A)
    sum_A = sum(A)
    sum_A -= max_A
    if sum_A + 1 < max_A :
        sum_A += sum_A + 1
    else :
        sum_A += max_A
    return sum_A

if __name__ == "__main__" :
    print(solution())