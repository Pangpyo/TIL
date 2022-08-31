# 2447 별 찍기10 G5


N = int(input())
stars = [['*']*N for _ in range(N)] # N*N의 별로 가득 찬 2차원 리스트를 만들어준다. 
def mkhole(n, a, b) : # 큰 N을 기준으로 a,b번째 칸부터 n크기의 정사각형에 공백 패턴을 찍어준다.
    n3 = n//3 # n/3값
    for i in range(n3+a*n, n3*2+a*n) :
        for j in range(n3+b*n, n3*2+b*n) :
            stars[i][j] = ' ' # 검사하는 정사각형의 가운데에 n/3 * n/3 의 공백을 만든다.
    if n >= 9 : # n이 9보다 클 때만 재귀한다.
        for i in range(3) :
            for j in range(3) : # n이 9 이상일때, 구역을 3*3으로 나누어 재귀적으로 패턴을 찍어준다.
                mkhole(n3, a*3+i, b*3+j)
mkhole(N, 0, 0)
for star in stars :
    print(*star, sep='')
