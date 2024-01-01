# 12888 포화 이진 트리 도로 네트워크 G4

def solution():
    n = int(input())
    D = [1]*(n+1)
    for i in range(2, n+1) :
        for j in range(i-1) :
            D[i] += D[j]*2
    return D[n]

if __name__ == "__main__" :
    print(solution())