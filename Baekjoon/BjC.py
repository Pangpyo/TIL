# C gahui and sousenkyo 3

def solution() :
    px, rx = map(int, input().split())
    vx = px/rx
    if vx < 0.2 :
        return "weak"
    elif vx < 0.4 :
        return "normal"
    elif vx < 0.6 :
        return "strong"
    else :
        return "very strong"
    

if __name__ == "__main__" :
    print(solution())