# 1449 수리공 항승 S3

from collections import deque

N, L = map(int, input().split())

loca = deque(sorted(list(map(int, input().split()))))  # 순서대로 정렬
cnt = 0  # 필요한 테이프 개수
while loca:  # 더 이상 커버할 위치가 없을 때 까지
    a = loca.popleft()  # 테이프를 붙힐 가장 왼쪽 위치를 pop 한후 a에 저장
    cnt += 1  # 테이프를 하나 사용했으므로 + 1
    while loca and loca[0] < a + L:  # 해당 테이프로 커버 할 수 있는 위치만큼 전부 pop해줌
        loca.popleft()
print(cnt)
# 메모리 32416kb 시간 92ms
