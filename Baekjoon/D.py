# D 오렌지먹은지오랜지


def solution():
    N = int(input())

    s = input()

    for i in range(1, N):
        cnt = 0
        for j in range(i):
            if s[j] != s[-i + j]:
                cnt += 1
        if cnt == 1:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(solution())
