# 1092 배 G5

from bisect import bisect

N = int(input())
crains = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())))
t = 0
if max(boxes) > max(crains):  # 크레인의 최대 수용무게보다 무거운 박스가 있을 경우 옮기지 못한다.
    print(-1)
else:
    while boxes:
        t += 1  # 시간
        for i in range(N):
            if not boxes:  # 더 이상 옮길 박스가 없는 경우 break
                break
            j = bisect(boxes, crains[i])
            # 내가 사용할 크레인과 같은 무게의 박스를 찾는다.(같은 무게가 없을 경우 해당 값을 넘지 않는 가장 큰 값을 찾아줌)
            if j:
                print(boxes.pop(j - 1))  # 해당 값을 pop한 후 출력한다.
    print(t)
# 메모리 32904 시간 248