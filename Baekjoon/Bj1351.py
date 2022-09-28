# 1351 무한 수열 G5

A = {0: 1}  # 무한수열 A의 모든 수를 구하는게 아닌, 필요한 수만 구할것이다.
# 그러므로 리스트를 만들어 인덱스로 접근하는게 아닌, 딕셔너리를 만들어 key로 접근한다.

N, P, Q = map(int, input().split())


def findAi(i):  # A수열의 i번째 수를 찾아주는 함수
    p = i // P  # i를 P로 나눈 수 중 가장 큰수, 즉 몫을 구한다.
    if p not in A:  # Ap 가 딕셔너리에 없을 경우 함수를 통해 새로 구해준다.
        findAi(p)
    q = i // Q
    if q not in A:
        findAi(q)
    A[i] = A[p] + A[q]  # A수열의 i번째 수를 구해준 후 리턴한다.
    return A[i]


if N == 0:
    print(A[0])
else:
    print(findAi(N))
