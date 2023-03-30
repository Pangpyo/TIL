# 8911 거북이 S3


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


class Turtle:
    x = 0
    y = 0
    d = 0
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0

    def __init__(self):
        pass

    def move(self, cmd):
        if cmd == "F":
            self.x += dx[self.d]
            self.y += dy[self.d]
        elif cmd == "B":
            self.x -= dx[self.d]
            self.y -= dy[self.d]
        elif cmd == "R":
            self.d = (self.d + 1) % 4
        else:
            self.d = (self.d - 1) % 4
        self.minx = min(self.minx, self.x)
        self.maxx = max(self.maxx, self.x)
        self.miny = min(self.miny, self.y)
        self.maxy = max(self.maxy, self.y)

    def square(self):
        return (self.maxx - self.minx) * (self.maxy - self.miny)


for t in range(int(input())):
    turtle = Turtle()
    cmds = input()
    for cmd in cmds:
        turtle.move(cmd)
    print(turtle.square())
