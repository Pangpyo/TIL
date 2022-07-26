# 2609 최대공약수와 최소공배수 B1

a, b = map(int,input().split())
A = [] #A의 약수가 들어갈 리스트

for i in range(1, a+1) :  
    if a%i == 0 :   #A의 약수를 구해줌
        A.append(i)
for j in range(1, b+1) :
    if b%j == 0 and j in A : #B의 약수를 구하며 A리스트에 있는지 확인
        G = j  #공약수를 G에 덮어씌움. 최종적으로는 최대공약수가 G에 남게됨

L = int(a*b/G) # 최소공배수는 a*b/G, 즉 두 수의 곱에서 최대공약수를 나눈 것임

print(G)
print(L)