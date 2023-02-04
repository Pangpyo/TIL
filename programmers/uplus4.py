from collections import deque


def solution(n, m, p):
    visit = set()
    que = deque([(n, m, 0, 0, 0, 1)])
    visit.add((n, m, 0, 0))

    def bfs():
        def move(n, m, nn, nm, s):
            if ms <= s <= p:
                sheeps.add((nn, nm))
            if n:
                move(n - 1, m, nn + 1, nm, s + 1)
            if m and (nn >= nm or not nn):
                move(n, m - 1, nn, nm + 1, s + 1)

        while que:
            n1, m1, n2, m2, cnt, loc = que.popleft()
            print(f"원래의 경우{n1, m1, n2, m2}, 횟수 : {cnt}")
            sheeps = set()
            if loc == 1:
                ms = 2
                move(n1, m1, 0, 0, 0)
            else:
                ms = 1
                move(n2, m2, 0, 0, 0)
            print("배 이동", sheeps, loc)
            print("방문", visit)
            for sn, sm in sheeps:
                nn1 = n1 - (sn * loc)
                nm1 = m1 - (sm * loc)
                nn2 = n2 + (sn * loc)
                nm2 = m2 + (sm * loc)
                if (nn1, nm1, nn2, nm2, loc) in visit:
                    continue
                if (nn1 >= nm1 or not nn1) and (nn2 >= nm2 or not nn2):
                    if nn1 == nm1 == 0:
                        return cnt + 1
                    print(f"경우의 수 {nn1, nm1, nn2, nm2}, 횟수 : {cnt + 1}")
                    visit.add((nn1, nm1, nn2, nm2, loc))
                    que.append((nn1, nm1, nn2, nm2, cnt + 1, -loc))
        return -1

    answer = bfs()
    return answer


print(solution(2, 2, 2))
