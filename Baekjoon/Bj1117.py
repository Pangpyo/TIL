# 1117 색칠 1 G5

def solution() :
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
    l = min(f, W-f)

    if x2 <= l :
        left = (x2 - x1) * (y2 - y1)
        right = 0
    elif x1 <= l and x2 > l :
        left = (l - x1) * (y2 - y1)
        right = (x2 - l) * (y2 - y1)
    else :
        left = 0
        right = (x2-x1) * (y2 - y1)
    under = left * 2 + right
    paint = under * (c+1)
    return W*H - paint

if __name__ == "__main__" :
    print(solution())