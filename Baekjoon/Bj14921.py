# 14921 용액 합성하기 G5

def solution():
    N = int(input())
    A = tuple(map(int, input().split()))
    s, e = 0, N-1
    answer = float('inf')
    while s < e:
        diff = A[s] + A[e]
        if abs(answer) > abs(diff):
            answer = diff
        if diff > 0:
            e -= 1
        elif diff < 0:
            s += 1
        else:
            return 0
    return answer

if __name__ == "__main__":
    print(solution())