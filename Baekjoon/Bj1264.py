# 1264 모음의 개수 B4

import sys

sys.stdin = open('input.txt')

vowel = ['a', 'e', 'i', 'o', 'u']

while 1 :
    words = input().lower() # 모두 소문자로 변환
    if words == '#' : # '#' 이 나오면 종료
        break
    ans = 0
    for i in vowel : # 각 모음의 개수 검사
        ans += words.count(i)
    print(ans)
