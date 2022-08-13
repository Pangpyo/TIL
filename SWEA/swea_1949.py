# 1949 등산로 조성 D4?
import sys

sys.stdin = open("_등산로조성.txt")

T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1] # 아래, 오른쪽, 위쪽, 왼쪽 순으로 방문 
def bfs(x, y, l) :
    global A
    if l > A :
        A = l
    for i in range(4) : # 4방향 방문
        nx = x + dx[i] # 방문 후의 좌표 정의
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N : # 인덱스 초과 방지
            continue
        if mountain[nx][ny] >= mountain[x][y] : # 오르막길일 경우
            continue
        if mountain[nx][ny] < mountain[x][y] : # 내리막 길인 경우
            bfs(nx, ny, l+1) # 해당 좌표를 방문 후 등산로 길이 +1
# bfs가 연속으로 가장 많이 실행된 횟수가 가장 긴 등산로의 길이가 된다.

        

def findpeak() :
    peak = max(map(max, mountain)) # 산의 봉우리를 찾아주는 함수
    peaks = []
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == peak :
                peaks.append((i, j))
    return peaks
    


for t in range(1, T+1) :
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    loads = []
    ans = 0
    for k in range(K+1) :
        for i in range(N) :
            for j in range(N) :
                mountain[i][j] -= k  # 모든 칸에 대해 k만큼 깎아 본 후 가장 긴 등산로를 구해본다.
                peaks = findpeak()
                if len(peaks) > 5 :
                    mountain[i][j] += k # 깎은 산 원상 복구
                for peak in peaks :
                    x, y = peak
                    A = 0
                    bfs(x, y, 1)
                    ans = A if A > ans else ans 
                mountain[i][j] += k  # 깎은 칸을 다시 복구해준다.

    print('#%d'%t, ans)
# 51개의 테스트케이스에서 50개만 통과했습니다...