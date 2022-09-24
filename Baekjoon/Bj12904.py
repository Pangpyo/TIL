# 12904 A와 B G5


S = input()
T = input()

while len(T) > len(S) :
    if T[-1] == 'A' :
        T = T[0:-1]
    else :
        T = T[0:-1][::-1]
    print(T)

if S == T :
    print(1)
else :
    print(0)