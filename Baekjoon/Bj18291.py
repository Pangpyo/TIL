# 18291 비요뜨의 징검다리 건너기 G5

def solution() :
    T = int(input())
    answers = [0]*T
    MAX = 1_000_000_007
    for t in range(T) :
        N = int(input())
        answer = 1
        if N > 2 :
            answer = pow(2, N-2, MAX)
        answers[t] = answer
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')