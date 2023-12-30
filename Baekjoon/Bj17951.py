# 17951 흩날리는 시험지 속에 내 평점이 느껴진거야 G4

def solution() :
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    total = sum(scores)
    s, e = 0, total+1
    
    answer = min(scores)
    while s <= e :
        mid = (s+e)//2
        cnt = 0
        div = 0
        for score in scores :
            div += score
            if div >= mid :
                div = 0
                cnt += 1
        if cnt < K :
            e = mid - 1
        else :
            s = mid + 1 
    answer = e
    return answer

if __name__ == "__main__" :
    print(solution())