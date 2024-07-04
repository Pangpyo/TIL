# 20164 홀수 홀릭 호석 G5

def solution():
    N = input()
    answer = [float('inf'), 0]
    def plus(*arg):
        temp = 0
        for a in arg:
            temp += int(a)
        return str(temp)

    def dfs(n, cnt):
        for a in n:
            if int(a)%2:
                cnt += 1
        if len(n) == 1:
            n = int(n)
            answer[0] = min(answer[0], cnt)
            answer[1] = max(answer[1], cnt)
        elif len(n) == 2:
            dfs(plus(n[0], n[1]), cnt)
        else:
            l = len(n)
            for i in range(l):
                for j in range(i+1, l):
                    for k in range(j+1, l):
                        dfs(plus(n[0:j], n[j:k], n[k::]), cnt)
    dfs(N, 0)
    return answer

if __name__ == "__main__":
    print(*solution())