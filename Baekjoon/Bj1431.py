# 1431 시리얼 번호 S3

N = int(input())
nums = []
for i in range(N) :
    nums.append(input())
numslist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 문자열에 숫자가 있는지 확인해줄 리스트
def numplus(string) : # 각 자리에 있는 숫자를 판별해주고 그 합을 출력해줄 함수
    ans = 0
    for s in string :
        if s in numslist :
            ans += int(s)
    return ans
nums = sorted(nums, key = lambda x : (len(x), numplus(x), x)) # 문자열의 길이순, 숫자들의 합, 문자열의 사전순으로 정렬
print(*nums, sep='\n') # 리스트를 한 줄씩 출력