# 18233 러버덕을 사랑하는 모임 G5

from itertools import combinations


N, P, E = map(int, input().split())

needs = []  # 회원들의 인형니즈

for i in range(N):
    x, y = map(int, input().split())
    needs.append((i, x, y))  # 니즈를 회원번호와 함께 저장


coms = list(combinations(needs, P))  # 조합으로 모든 경우의 수를 구한다


def answer(N, E):
    for com in coms:  # 모든 조합 검사
        minsum = 0  # 해당 조합에서 회원들이 요구하는 인형 개수의 최소값
        maxsum = 0  # 해당 조합에서 회원들이 요구하는 인형 개수의 최대값
        ans = [0] * N  # 답이 들어갈 리스트
        maxes = [0] * N  # 각 회원들이 요구하는 인형의 최대 인형이 들어갈 리스트
        for c in com:
            minsum += c[1]
            maxsum += c[2]
            ans[c[0]] += c[1]  # 우선은 답이 들어갈 리스트에 최소값을 넣어준다
            maxes[c[0]] += c[2]
        if minsum <= E <= maxsum:  # 최소값 <= 줄 인형의 개수 <= 최대값인 경우에만
            sumdiff = E - minsum  # 남는 인형의 개수
            for i in range(N):
                if ans[i]:
                    diff = maxes[i] - ans[i]  # i번째 회원이 원하는 인형의 최대와 최소의 차이
                    if diff < sumdiff:  # 그 차이가 지금 가지고 있는 인형보다 적을 경우
                        ans[i] += diff  # 그 차이만큼 인형을 더해주고
                        sumdiff -= diff  # 인형 개수가 그만큼 줄어들게 한다
                    else:  # 그 차이가 지금 가지고 있는 인형보다 클 경우
                        ans[i] += sumdiff  # 남은 인형을 모두 주고
                        return ans  # ans를 리턴한다.
    return -1  # 이 과정을 모두 거치고도 함수가 종료되지 않았으면, -1을 리턴한다.


ans = answer(N, E)

if ans == -1:
    print(-1)
else:
    print(*ans)
