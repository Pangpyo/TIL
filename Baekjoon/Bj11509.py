# 11509 풍선 맞추기 G5

def solution() :
    N = int(input())
    B = list(map(int, input().split()))
    arrows = [0]*(max(B)+1)
    for b in B :
        if not arrows[b] :
            arrows[b] += 1
        arrows[b] -= 1
        arrows[b-1] += 1
    return sum(arrows)

if __name__ == "__main__" :
    print(solution())
