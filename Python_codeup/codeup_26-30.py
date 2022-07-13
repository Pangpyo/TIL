# 6026
# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

a = input()
b = input()
c = float(a) + float(b)
print(c)

# 6027
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

a_10 = int(input())

print('%x'%a_10) # %x : 16진수 표기(hex)

# 6028
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

a_10 = int(input())

print('%X'%a_10) # %X : 16진수 대문자 표기(HEX)

# 6029
# 16진수를 입력받아 8진수(octal)로 출력해보자.

a_16 = int(input(),16)

print('%o'%a_16)

# 6030
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

n = ord(input())
print(n)