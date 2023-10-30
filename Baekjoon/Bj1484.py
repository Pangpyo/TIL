# 1484 다이어트 G5

def solution() :
    G = int(input())
    ans = []
    a = 1
    i = 1
    while a + i < 100001 :
        temp = G + i*i
        while temp >= a*a :
            if temp <= a*a :
                if temp == a*a :
                    ans.append(a)
                break
            else :
                a += 1
        i += 1
        

    return ans if ans else [-1]

if __name__ == "__main__" :
    print(*solution(), sep='\n')