# 1406 에디터 S2

import sys

input = sys.stdin.readline

front = list(input().rstrip())

back = []


for i in range(int(input())):
    cmd = input().rstrip()

    if cmd == "L":
        if front:
            back.append(front.pop())
    elif cmd == "D":
        if back:
            front.append(back.pop())
    elif cmd == "B":
        if front:
            front.pop()
    else:
        front.append(cmd[2])


print("".join(front + back[::-1]))
