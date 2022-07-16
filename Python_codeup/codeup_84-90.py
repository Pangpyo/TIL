# 6084
# 소리 파일 저장용량 계산하기


s, h, b, c = map(int, input().split())

mb = s*h*b*c/8/1024/1024

print('%.1f'%mb, 'MB')