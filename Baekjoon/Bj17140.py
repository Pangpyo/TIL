# 17140 이차원 배열과 연산 G4


r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]

def RC(A) :
    nA = []
    maxl = 0
    for nums in A :
        dic = {}
        for n in nums :
            if n == 0 :
                continue
            if n not in dic :
                dic[n] = 1
            else :
                dic[n] += 1
        nnums = []
        for k, v in dic.items() :
            nnums.append((k, v))
        nnums = sorted(nnums, key=lambda x : (x[1], x[0]))
        fnums = ()
        for n in nnums :
            fnums += n
        maxl = len(fnums) if len(fnums) > maxl else maxl
        fnums = fnums[0:100]
        nA.append(list(fnums))
    for nums in nA :
        nums += [0]*(maxl-len(nums))
    return nA

def flip(A) :
    row = len(A)
    col = len(A[0])
    rA = [[0]*row for _ in range(col)]
    for i in range(col) :
        for j in range(row) :
            rA[i][j] = A[j][i]
    return rA
cnt = 0
while 1 :
    row = len(A)
    col = len(A[0])
    if r-1 >= row or c-1 >= col :
        pass
    elif A[r-1][c-1] == k :
        break
    if cnt == 100 :
        cnt = -1
        break
    cnt += 1

    if row >= col :
        A = RC(A)
    else :
        A = flip(RC(flip(A)))
print(cnt)
