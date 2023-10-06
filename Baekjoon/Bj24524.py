# 24524 아름다운 문자열 G5

from collections import defaultdict, deque


def solution() :
    S = input()
    T = input()
    dic = defaultdict(deque)
    for i, c in enumerate(S) :
        dic[c].append(i)
    ans = 0
    flag = True
    while flag:
        pre = -1
        for c in T :
            while dic[c]:
                temp = dic[c].popleft()
                if temp > pre :
                    pre = temp
                    break
            else :
                flag = False
                break
        if flag :
            ans += 1
    return ans

if __name__ == "__main__" :
    print(solution())