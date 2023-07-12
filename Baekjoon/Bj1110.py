# 1110 더하기 사이클 B1

def solution() :
    N = int(input())
    a = N # 변화할 주어진 수
    b = 0 # a의 각 자리의 합
    count = 0 #사이클의 길이
    while 1 :
        b = a//10 + a%10 
        # a는 항상 두자리 수이므로 각 자리 수의 합은 10으로 나눈 몫과 나머지의 합이다.
        a = (a%10)*10+ b%10
        # a는 이전 a의 1의자리가 10의자리가 되고, b의 1의자리가 1의자리가 된다.
        count += 1 #사이클의 길이가 더해진다
        if a == N : #a가 가장 처음 주어졌던 N과 같아지면 사이클의 길이를 출력하고 반복문을 종료한다.
            return count

if __name__ == "__main__" :
    print(solution())
            