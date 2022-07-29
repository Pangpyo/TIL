# 1357 뒤집힌덧셈 B1

X, Y = input().split()

X = int(X[::-1])
Y = int(Y[::-1])
XY = str(X+Y)[::-1]
print(int(XY))