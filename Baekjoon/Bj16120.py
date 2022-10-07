# 16120 PPAP G4

word = input()


def solution(word):
    stack = []
    for i in range(len(word)):
        stack.append(word[i])
        if len(stack) >= 4:
            if "".join(stack[-4::]) == "PPAP":
                for _ in range(3):
                    stack.pop()
    stack = "".join(stack)
    if stack == "P":
        return "PPAP"
    else:
        return "NP"


print(solution(word))
