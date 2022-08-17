# 2839 설탕배달 S4

N = int(input())
ans = -1
for i in range((N//5), -1, -1) :
    if (N-5*i)%3 == 0 :
        ans = i + (N-5*i)//3
        break
print(ans)