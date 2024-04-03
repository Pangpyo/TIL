# 24552 올바른 괄호 G4

def solution():
    S = input()
    sums, l, r = 0, 0, 0
    for s in S:
        if s == '(':
            sums += 1
            l += 1
        else:
            sums -= 1
            r += 1
        if sums < 0 :
            return r
        elif sums == 0:
            l = 0
    return l

if __name__ == "__main__":
    print(solution())