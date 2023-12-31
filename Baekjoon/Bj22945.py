# 22945 팀 빌딩 G4

def solution() :
    N = int(input())
    MAX = 10000
    min_idx = [N+2]*(MAX+1)
    max_idx = [0]*(MAX+1)
    for i, n in enumerate(map(int, input().split())) :
        min_idx[n] = min(min_idx[n], i+1)
        max_idx[n] = max(max_idx[n], i+1)
    answer = 0
    for i, s in enumerate(min_idx) :
        if s == N+2 :
            continue
        for j, b in enumerate(max_idx) :
            if not b or s == b:
                continue
            answer = max(answer, min(i, j)*(abs(b-s)-1))

    return answer

if __name__ == "__main__" :
    print(solution())