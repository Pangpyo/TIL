# 1863 스카이라인 쉬운거 G4
import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    stack = [0]
    answer = 0
    for i in range(N+1):
        if i == N :
            y = 0
        else :
            x, y = map(int, input().split())

        while stack and stack[-1] > y:
            y = min(stack.pop(), y)
            answer += 1
        else :
            if not stack or stack[-1] != y :
                stack.append(y)

    return answer

if __name__ == "__main__":
    print(solution())