# 23048 자연수 색칠하기 G5

def solution():
    N = int(input())
    answer = [0]*(N)
    c = 1
    answer[0] = 1
    for i in range(1, N):
        if answer[i]:
            continue
        c += 1
        for j in range(i, N, i+1):
            answer[j] = c
    print(c)
    return answer

if __name__ == "__main__":
    print(*solution())