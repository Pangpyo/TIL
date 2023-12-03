# A gahui and sousenkyo 1

def solution() :
    chars = tuple(map(int, input().split()))
    answer = 0
    for i in range(1, 5) :
        if chars[0]-chars[i] <= 1000 :
            answer += 1
    return answer

if __name__ == "__main__" :
    print(solution())