# 1461 도서관 G5

N, M = map(int, input().split())

books = list(map(int, input().split()))

leftbooks = []
rightbooks = []
lastbook = False

maxbook = 0
for book in books:
    if abs(book) > maxbook:
        maxbook = abs(book)
        if book < 0:
            lastbook = False
        else:
            lastbook = True
    if book < 0:
        leftbooks.append(-book)
    else:
        rightbooks.append(book)

leftbooks.sort()
rightbooks.sort()

ans = 0

if not lastbook:
    while rightbooks:
        walk = 0
        walk += rightbooks.pop()
        ans += walk * 2

        for i in range(M - 1):
            if not rightbooks:
                break
            rightbooks.pop()
    first = True
    while leftbooks:
        walk = 0
        walk += leftbooks.pop()
        if first:
            ans += walk
            first = False
        else:
            ans += walk * 2
        for i in range(M - 1):
            if not leftbooks:
                break
            leftbooks.pop()
else:
    while leftbooks:
        walk = 0
        walk += leftbooks.pop()
        ans += walk * 2

        for i in range(M - 1):
            if not leftbooks:
                break
            leftbooks.pop()
    first = True
    while rightbooks:
        walk = 0
        walk += rightbooks.pop()
        if first:
            ans += walk
            first = False
        else:
            ans += walk * 2

        for i in range(M - 1):
            if not rightbooks:
                break
            rightbooks.pop()
print(ans)
