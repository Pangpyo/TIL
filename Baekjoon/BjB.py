# B gahui and sousenkyo 2

def solution() :
    n = int(input())
    mine = int(input())
    others = tuple(map(int, input().split()))
    rank = 1
    for other in others :
        if other > mine :
            rank += 1
    return rank

if __name__ == "__main__" :
    print(solution())