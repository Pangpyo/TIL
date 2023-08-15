# 1062 가르침 G4

def solution() :
    N, K = map(int, input().split())
    def toBit(word) :
        bit = 0
        for w in word :
            bit |= 1<<(ord(w)-ord('a'))
        return bit
    need = toBit("antatica")
    wordsBit = []
    for i in range(N) :
        wordsBit.append(toBit(input()))
    K -= 5
    if K < 0 :
        return 0
    answer = 0
    def comb(n, cnt, comp) :
        nonlocal answer
        if cnt == K :
            answer = max(compare(comp), answer)
            return
        for i in range(n, 26) :
            if comp&(1<<i) :
                continue
            comb(i, cnt+1, comp|(1<<i))
    def compare(comp) :
        canRead = 0
        for word in wordsBit :
            if (word&comp) == word :
                canRead += 1
        return canRead
    
    comb(0, 0, need)

    return answer

if __name__ == "__main__" :
    print(solution())