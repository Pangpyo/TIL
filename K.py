# 케이크 두개

from fractions import Fraction


def solution() :
    points = []
    for _ in range(8):
        x, y = map(Fraction, input().split())
        points.append((x, y))

    top_rectangle = points[:4]
    bottom_rectangle = points[4:]


    top_x_mid = (max(top_rectangle, key=lambda p: p[0])[0] + min(top_rectangle, key=lambda p: p[0])[0]) / 2
    top_y_mid = (max(top_rectangle, key=lambda p: p[1])[1] + min(top_rectangle, key=lambda p: p[1])[1]) / 2
    bottom_x_mid = (max(bottom_rectangle, key=lambda p: p[0])[0] + min(bottom_rectangle, key=lambda p: p[0])[0]) / 2
    bottom_y_mid = (max(bottom_rectangle, key=lambda p: p[1])[1] + min(bottom_rectangle, key=lambda p: p[1])[1]) / 2

    a = (top_y_mid - bottom_y_mid) / (top_x_mid - bottom_x_mid)
    b = top_y_mid - a * top_x_mid

    return a, b

if __name__ == "__main__" :
    print(*solution())