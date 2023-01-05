# 1034 램프 G4

N, M = map(int, input().split())

table = [input() for _ in range(N)]

K = int(input())

dic = {}

for t in table:  # 같은 배열의 개수를 딕셔너리로 세어준다.
    if t in dic:
        dic[t] += 1
    else:
        dic[t] = 1

dic = list(dic.items())  # items를 사용해 키와 밸류로 만들어 리스트로 만들어준다

dic.sort(key=lambda x: -x[1])  # 개수 순으로 정렬한다


def answer():
    for t, n in dic:
        cnt = t.count("0")
        if K >= cnt and (K - cnt) % 2 == 0:
            # 해당 배열을 켜진 상태로 만드려면 해당 배열의 꺼진 전구의 수보다 스위치를 누르는 횟수가 더 커야한다.
            # 또한 0인 부분들을 모두 키고 남은 횟수가 짝수여야한다. 짝수이면 같은것을 껐다 켰다 하면서 원상태로 되돌릴 수 있기 때문이다.
            return n
    return 0


print(answer())
