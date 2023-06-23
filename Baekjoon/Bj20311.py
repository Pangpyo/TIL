# 20311 화학 실험 G5


from heapq import heappop, heappush


def solution() :
    N, K = map(int, input().split())
    c = []
    for i, n in enumerate(map(int, input().split())) :
        heappush(c, (-n, i+1))
    flag = True
    ans = []
    temp = []
    while c :
        n, i = heappop(c)
        ans.append(i)
        if len(ans) >= 2 and ans[-1] == ans[-2] :
            flag = False
            break
        if temp :
            x = temp.pop()
            if x[0] < 0 :
                heappush(c, x)
        temp.append((n+1, i))
    if not flag or temp[0][0] <= -1 :
        return [-1]

    return ans

if __name__ == "__main__" :
    print(*solution())