# 2806 DNA 발견 G4

def solution():
    N = int(input())
    DNA = input()
    D = [[0, 0] for _ in range(N)]
    B = 0
    for i, d in enumerate(DNA):
        if d == 'A':
            B = 0
            D[i][0] = D[i-1][0]
            D[i][1] = min(D[i-1][0]+1, D[i-1][1]+1)
        else :
            B += 1
            D[i][0] = min(D[i-1][0]+1, D[i-B][1]+1)
            D[i][1] = D[i-1][1]
    return D[-1][0]

if __name__ == "__main__":
    print(solution())