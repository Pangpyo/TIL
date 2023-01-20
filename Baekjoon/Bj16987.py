# 16987 계란으로 계란치기 G5


N = int(input())

eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def crush_egg(n) :
	global ans
	if n == N :
		egga = [eggs[i][0] for i in range(N)]
		crushed = 0
		for i in range(N) :
			if egga[i] <= 0 :
				crushed += 1 
		ans = max(crushed, ans)
		return
	if eggs[n][0] <= 0 :
		crush_egg(n+1)
		return
	for i in range(N) :
		if n == i :
			continue
		if eggs[i][0] <= 0 :
			crush_egg(n+1)
			continue
		eggs[i][0] -= eggs[n][1]
		eggs[n][0] -= eggs[i][1]
		crush_egg(n+1)
		eggs[i][0] += eggs[n][1]
		eggs[n][0] += eggs[i][1]



crush_egg(0)

print(ans)