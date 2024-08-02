# 28015 영역 색칠 S2

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    answer = 0
    for _ in range(N):
        line = tuple(map(int, input().split()))
        temp = 0
        use = [0, 0]
        cnt = [0, 0]
        for l in line:
            if l:
                if l == 1:
                    if not use[0]:
                        use[0] = 1
                        cnt[0] += 1
                    use[1] = 0
                else:
                    if not use[1]:
                        use[1] = 1
                        cnt[1] += 1
                    use[0] = 0
            else:
                if sum(use):
                    temp += min(cnt) + 1
                use = [0, 0]
                cnt = [0, 0]
        if sum(cnt):
            temp += min(cnt) + 1
        answer += temp
        
    return answer

if __name__ == "__main__":
    print(solution())