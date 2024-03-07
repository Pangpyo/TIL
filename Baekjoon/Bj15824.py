# 15824 너 봄에는 캡사이신이 맛있단다 G2

def solution() :
    N = int(input())
    menu = list(map(int, input().split()))
    menu.sort()
    MOD = 1_000_000_007
    answer = 0
    for i in range(N) :
        answer += menu[i] * (pow(2, i, MOD) - pow(2, N - i - 1, MOD))
    return answer % MOD

if __name__ == "__main__" :
    print(solution())