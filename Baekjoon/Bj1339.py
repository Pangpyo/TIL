# 1339 단어수학 G4

ans = 0
dic = {}
words = []
for i in range(int(input())):
    word = input()
    l = len(word)
    words.append((word, l))

    for i in range(l):
        if word[i] not in dic:
            dic[word[i]] = 10 ** (l - i - 1)
        else:
            dic[word[i]] += 10 ** (l - i - 1)
dic = sorted(dic.items(), key=lambda x: -x[1])
dicnum = {}
n = 9
for k, v in dic:
    dicnum[k] = n
    n -= 1
for word, l in words:
    for i in range(l):
        ans += dicnum[word[i]] * (10 ** (l - i - 1))
print(ans)
