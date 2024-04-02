# 15927 회문은 회문아니야!! G5

def solution():
    S = input()
    N = len(S)
    if S == S[0]*N :
        return -1
    elif S == S[::-1]:
        return N-1
    else :
        return N

if __name__ == "__main__":
    print(solution())