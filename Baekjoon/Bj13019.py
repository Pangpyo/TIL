# 13019 A를 B로 G4

def solution() :
    A, B = input(), input()
    alpha = [0]*27
    ZERO = ord('A')
    for a, b in zip(A, B) :
        alpha[ord(a)-ZERO] += 1
        alpha[ord(b)-ZERO] -= 1
    for a in alpha :
        if a :
            return -1
    N = len(A)
    idx = N
    cnt = 0
    for b in reversed(B) :
        flag = True
        for i in reversed(range(idx)) :
            if A[i] == b :
                idx = i
                flag = False
                cnt += 1
                break
        if flag :
            break
        
    return N - cnt

if __name__ == "__main__" :
    print(solution())