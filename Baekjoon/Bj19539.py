# 19539 사과나무 G5

def solution():
    N = int(input())
    trees = tuple(map(int, input().split()))
    s = sum(trees)
    if s%3:
        return "NO"
    day = s//3
    cnt = sum((tree//2 for tree in trees))
    if cnt < day:
        return "NO"
    return "YES"

if __name__ == "__main__":
    print(solution())