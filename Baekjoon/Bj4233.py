# 4233 가짜소수 G5

def solution() :
    answer = []
    while True :
        p, a = map(int, input().split())
        if p == a == 0 :
            break
        ans = 'yes'
        isPrime = True
        for i in range(2, int(p**0.5)+1) :
            if not p % i :
                isPrime = False
                break
        if isPrime or pow(a, p, p) != a :
            ans = ('no')
        answer.append(ans)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')