# 2587 대표값2 B2
s = []

for i in range(5) : 
    s.append(int(input()))
    
s = sorted(s)
print(int(sum(s)/5))
print(s[2])