# 9935 문자열 폭발 G4


word, bomb = input(), input()


def answer(word, bomb):
    stack = []
    bl = len(bomb)
    for i in range(len(word)):
        stack.append(word[i])
        if len(stack) >= bl:
            tmp = "".join(stack[-bl:])
            if tmp == bomb:
                for _ in range(bl):
                    stack.pop()
    ans = "".join(stack)
    return ans if ans else "FRULA"


print(answer(word, bomb))
