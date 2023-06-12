# 2661 좋은수열 G4

def solution() :
    N = int(input())
    A = [0]*N
    def bt(n) :
        if n == N :
            print(*A, sep="")
            exit()
        for i in range(1, 4) :
            A[n] = i
            flag = True
            for j in range((n+1)//2) :
                if A[n-2*j-1:n-j] == A[n-j:n+1] :
                    flag = False
                    break  
            if flag :
                bt(n+1)
    bt(0)

if __name__ == "__main__" :
    solution()



