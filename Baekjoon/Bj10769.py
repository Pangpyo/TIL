# 10769 행복한지 슬픈지 B1

text = input()

smile = text.count(':-)')
wry = text.count(':-(')


if smile == 0 and wry == 0 :
    print('none')
elif smile == wry :
    print('unsure')
elif smile > wry :
    print('happy')
elif smile < wry :
    print('sad')