# 1360 되돌리기 G5

import sys


sys.stdin = open("input.txt")


N = int(input())
stack = []  # 우선 모든 명령어를 스택에 쌓아둔다


def undo(t, s):
    i = 0
    diff = s - t
    for i in range(len(stack)):
        if s > stack[i][2] >= diff:  # 해당하는 시간 내에 있는 명령어들의 실행 여부를 뒤바꿔준다.
            stack[i][3] = not stack[i][3]


for i in range(N):
    command, x, s = input().split()
    if command == "type":  # type인 경우 1로
        stack.append([1, x, int(s), True])
    elif command == "undo":  # undo인 경우 2로 스택에 저장한다. 그리고 리스트의 마지막에 해당 명령어를 실행할지 말지 구분한다
        stack.append([2, int(x), int(s), True])

if N == 0:
    pass
else:
    for i in range(N - 1, -1, -1):  # 뒤쪽부터 역순으로 봐서 각 명령어에 대해 undo를 실행한다
        if stack[i][0] == 2 and stack[i][3]:
            undo(stack[i][1], stack[i][2])

    for i in range(N):  # 앞쪽부터 type들만 실행해 하나씩 출력한다
        if stack[i][0] == 1 and stack[i][3]:
            print(stack[i][1], end="")
