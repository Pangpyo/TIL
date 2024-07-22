# 23304 아카라카 S2

def solution():
    S = input()
    def is_arakara(S):
        N = len(S)
        if N <= 1:
            return True
        l = S[0:N//2]
        r = S[(N+1)//2::]
        return S == S[::-1] and is_arakara(l) and is_arakara(r)
    if is_arakara(S):
        return "AKARAKA"
    else:
        return "IPSELENTI"


if __name__ == "__main__":
    print(solution())