# 13164 행복 유치원 G5

N, K = map(int, input().split())

children = list(map(int, input().split()))
diff = []
for i in range(1, N):
    diff.append(children[i] - children[i - 1])  # 각 유치원생의 키 차이를 저장
# 1 3 5 6 10 유치원생들의 키
#  2 2 1 4   키 차이
# 한 조 안에서 비용은 키 차이를 모두 합한 값과 같다. (2+2+1+4 = 9, 10 - 1 = 9)
# 조를 하나 만든다는 것은 이 키 차이 중 하나를 뺀다는것과 같다
# 예시로 K가 2일경우, 조를 2개로 만들어야 한다.
# 키 차이가 가장 크게 나는 구간인 6과 10을 나누면
# 1 3 5 6 / 10
#  2 2 1
# 총 비용이 4 줄어들게 된다.
# K가 3일 경우는 키 차이가 큰 순으로 2개 뺀다.
# 1 / 3 5 6 / 10    1 3 / 5 6 / 10
#      1 2           2     1
# 키 차이가 가장 큰 4를 뺀 후에는, 키 차이가 2인 어느 곳을 빼던 결과는 같다.
# 그러므로 N개의 유치원생들을 K개의 조를 만들어 티셔츠 비용이 최소가 되게 하는 것은
# N - 1개의 키 차이에서 K - 1개의 키 차이를 빼 최소가 되게 하는 것과 같다.
# 그러므로 키 차이가 가장 큰 K - 1개의 키 차이만을 빼주면 문제는 해결된다.
diff.sort()  # 키 차이를 순서대로 정렬한다
for i in range(K - 1):  # 키 차이를 큰 순서대로 K - 1개를 빼준다
    diff.pop()
print(sum(diff))  #  나머지 키 차이를 모두 합해준다.
# 메모리 64824 시간 304