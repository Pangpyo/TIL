# 2559 수열 S3

import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())

tems = list(map(int, input().split()))

sumtems = [0, tems[0]] # 누적합 알고리즘을 사용했다.

for i in range(1, N) :
    sumtems.append(tems[i]+sumtems[i]) # 누적합 수열을 구한다.

maxK = sumtems[K] # 누적합 수열의 K번째 인덱스를 max값으로 초기 설정한다.
for i in range(N-K+1) :
    temK = sumtems[K+i]-sumtems[i] 
# 누적합 수열의 K+i번째 인덱스에서 i번째 인덱스를 빼면 i번째 인덱스부터 K개의 합을 구할 수 있다.
    maxK = temK if temK > maxK else maxK # 그 값을 maxK와 비교해서 큰 값을 넣는다.
print(maxK)