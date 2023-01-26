# 3425 고스택 G3

import sys

input = sys.stdin.readline


stack = []


def NUM(X):
    stack.append(X)
    return True


def POP():
    if len(stack) >= 1:
        stack.pop()
        return True
    else:
        return False


def INV():
    if len(stack) >= 1:
        a = stack.pop()
        stack.append(-a)
        return True
    else:
        return False


def DUP():
    if len(stack) >= 1:
        stack.append(stack[-1])
        return True
    else:
        return False


def SWP():
    if len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
        return True
    else:
        return False


def ADD():
    if len(stack) >= 2:
        a, b = stack.pop(), stack.pop()
        if abs(a + b) > 10**9:
            return False
        stack.append(a + b)
        return True
    else:
        return False


def SUB():
    if len(stack) >= 2:
        a, b = stack.pop(), stack.pop()
        if abs(b - a) > 10**9:
            return False
        stack.append(b - a)
        return True
    else:
        return False


def MUL():
    if len(stack) >= 2:
        a, b = stack.pop(), stack.pop()
        if abs(a * b) > 10**9:
            return False
        stack.append(a * b)
        return True
    else:
        return False


def DIV():
    if len(stack) >= 2:
        a, b = stack.pop(), stack.pop()
        if a == 0:
            return False
        pm = 1
        if a < 0:
            pm *= -1
        if b < 0:
            pm *= -1
        stack.append(pm * (abs(b) // abs(a)))
        return True
    else:
        return False


def MOD():
    if len(stack) >= 2:
        a, b = stack.pop(), stack.pop()
        if a == 0:
            return False
        pm = -1 if b < 0 else 1
        stack.append(pm * (abs(b) % abs(a)))
        return True
    else:
        return False


while 1:
    command = []
    cmd = True
    while 1:
        a = input()
        if a.rstrip() == "END":
            cmd = False
            continue
        elif a.rstrip() == "QUIT":
            quit()
        if cmd:
            command.append(tuple(a.rsplit()))
        else:
            v = [int(input()) for _ in range(int(a))]
            for n in v:
                stack = [n]
                rst = True
                for c in command:
                    if c[0] == "NUM":
                        rst = NUM(int(c[1]))
                    elif c[0] == "POP":
                        rst = POP()
                    elif c[0] == "INV":
                        rst = INV()
                    elif c[0] == "DUP":
                        rst = DUP()
                    elif c[0] == "SWP":
                        rst = SWP()
                    elif c[0] == "ADD":
                        rst = ADD()
                    elif c[0] == "SUB":
                        rst = SUB()
                    elif c[0] == "MUL":
                        rst = MUL()
                    elif c[0] == "DIV":
                        rst = DIV()
                    elif c[0] == "MOD":
                        rst = MOD()
                    if not rst:
                        break
                if len(stack) != 1 or not rst:
                    print("ERROR")
                else:
                    print(stack[0])
            input()
            print()
            break
