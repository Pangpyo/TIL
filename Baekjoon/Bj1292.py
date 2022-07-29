# 1292 쉽게푸는 문제 B1

a, b = map(int, input().split())

A = [] #수열을 저장할 리스트
point = 0
for i in range(b+1) : #수열을 만듦.
    for j in range(i) : 
        A.append(i)
        if len(A) == b : #b와 같은 길이가 됐을 경우 연산을 줄이기 위해 break
            point += 1
            break
    if point == 1 : #b와 같은 길이가 됐을 경우 연산을 줄이기 위해 break
        break
print(sum(A[a-1:b]))
