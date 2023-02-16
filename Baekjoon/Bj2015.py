# 2015 수들의 합4 G4

from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * N

dic = defaultdict(int)

ans = 0

for i in range(N):
    D[i] = D[i - 1] + A[i]  # 1. 누적합을 하나씩 만들어주면서
    if D[i] - K in dic:  # 4. 지금 검사하는 누적합 -K가 딕셔너리에 몇개 있는지 세어주고 ans에 그 개수만큼 넣어준다
        ans += dic[D[i] - K]
    dic[D[i]] += 1  # 2. 그 누적합을 딕셔너리에 넣어준다
    if D[i] == K:  # 3. 그 누적합 자체가 K면 하나 더해준다
        ans += 1
    print(i, D, ans, dic)

print(ans)
