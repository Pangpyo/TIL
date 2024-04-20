# 31433 KSA 문자열 G5

def solution():
    X = input()
    N = len(X)
    def check(X, N):
        dic = {'K':0, 'S':1, 'A':2}
        idx = 0
        cnt = 0
        for x in X:
            if idx%3 == dic[x]:
                idx += 1
            else :
                cnt += 1
        return abs(N-idx) + cnt
    answer = min(check(X, N), check('K'+X, N)+1, check('KS'+X, N)+2)
    return answer 

if __name__ == "__main__":
    print(solution())