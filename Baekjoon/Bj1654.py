# 1654 랜선 자르기 S2

import sys


input = sys.stdin.readline  # 입력이 많으므로 표준입력

K, N = map(int, input().split())

lines = []  # 선들이 저장될 리스트

for i in range(K):
    lines.append(int(input()))
start = 1  # 나올 수 있는 랜선의 최소길이와 최대길이
end = max(lines)  # 최대길이
ans = 0  # 답이 저장될 변수
while start <= end:
    mid = (start + end) // 2  # 이분탐색을 한다. 최대길이와 최소길이의 중간값으로 잘라준다
    cnt = 0  # 몇개로 잘라졌는지 세어준다
    for line in lines:  # 모든 line들을 mid만큼 잘라준다
        cnt += line // mid  # 몇개로 잘랐는지 세어준다
    if cnt >= N:  # 개수가 N 이상일 경우
        start = mid + 1  # 최소길이를 mid + 1로 설정해 길이를 늘려주도록 한다.
        ans = max(ans, mid)  # 이 때 랜선의 최대 길이를 구하기 위해 항상 이전의 값과 비교에 넣어준다
    else:
        end = mid - 1  # 개수가 N 미만일 경우 최대길이를 mid-1로 설정해 길이를 줄여준다

print(ans)
