# 2607 비슷한 단어 S3


N = int(input())

wl = [0] * 26  # 기준 단어의 알파벳들의 개수를 세어줄 리스트

word = input()

for w in word:
    wl[ord(w) - 65] += 1  # 아스키코드값으로 세어준다~!


ans = 0
for i in range(N - 1):
    nword = input()
    nwl = [0] * 26  # 새 단어도 마찬가지로 세어준다
    for w in nword:
        nwl[ord(w) - 65] += 1
    p = 0  # 기준 단어가 더 많이 가지고 있는 글자의 수
    m = 0  # 기준 단어가 더 적게 가지고 있는 글자의 수
    for i in range(26):
        if wl[i] > nwl[i]:
            p += wl[i] - nwl[i]
        else:
            m += nwl[i] - wl[i]
    if p <= 1 and m <= 1:  # 각각이 1 이하여야 한다
        ans += 1

print(ans)
