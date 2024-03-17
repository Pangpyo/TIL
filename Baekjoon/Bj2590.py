# 2590 색종이 G4

def solution() :
    papers = [0] + list(int(input()) for _ in range(6))
    block = [0]*7
    answer = 0
    answer += sum(papers[4::])
    block[1] += 11*papers[5]
    block[2] += 5*papers[4]
    answer += papers[3]//4 + 1
    if papers[3]%4 == 1 :
        block[2] += 5
        block[1] += 7
    elif papers[3]%4 == 2 :
        block[2] += 3
        block[1] += 6
    elif papers[3]%4 == 3 :
        block[2] += 1
        block[1] += 5
    else :
        answer -= 1
    
    if papers[2] > block[2] :
        papers[2] -= block[2]
        answer += papers[2]//9 + (1 if papers[2]%9 else 0)
        block[1] += (9 - papers[2]%9)*4 if papers[2]%9 else 0
    else :
        block[2] -= papers[2]
        block[1] += block[2]*4

    if papers[1] > block[1] :
        papers[1] -= block[1]
        answer += papers[1]//36 + (1 if papers[1]%36 else 0)
    
    return answer

if __name__ == "__main__" :
    print(solution())