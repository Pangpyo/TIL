# 5582 공통 부분 문자열 G5

def solution() :
    A, B = input(), input()
    def compare(A, B) :
        ans = 0
        N, M = len(A), len(B)    
        for i in range(M) :
            temp = 0
            for j in range(min(M-i, N)) :
                if A[j] == B[i+j] :
                    temp += 1
                    ans = max(temp, ans)
                else :
                    temp = 0
        return ans
    ans = max(compare(A, B), compare(B, A))
    return ans

if __name__ == "__main__" :
    print(solution())