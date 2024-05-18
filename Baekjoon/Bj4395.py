# 4395 Steps G5

def solution():
    T = int(input())
    answers = [0]*T
    for t in range(T):
        a, b = map(int, input().split())
        diff = b - a
        if diff == 0:
            continue
        x = int(diff**0.5)
        d, m = divmod(diff-x*x, x)
        answer = x*2-1 + d + int(m>0)
        answers[t] = answer
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')