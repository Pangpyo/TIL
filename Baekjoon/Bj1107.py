# 1107 리모컨 G5



N = int(input())
M = int(input())
if M : # 부서진 키가 존재 하는 경우
    brokens = list(map(int, input().split())) # 부서진 버튼들의 리스트를 작성
else : # 부서진 버튼이 존재하지 않을 경우, 두번째 인풋을 받지 않기 위해 예외 작성
    brokens = []
if M != 10 : # 부서진 버튼이 10개 아닌 경우
    ans = 0 # 답을 저장할 변수
    i = 0 # while문에서 증가할 변수
    stop = False # while문을 멈출 트리거
    while 1 : 
        check = False # 검사하는 수가 버튼으로 누를 수 있는 수인지 검사
        for pm in [-1, +1] : # 음수와 양수
            for n in str(N+i*pm) : # N에서 i만큼 빼거나 더한 값이 누를 수 있는 값인지 한 숫자씩 검사함
                if N+i*pm < 0 : # 음수는 검사하지 않음
                    continue
                if int(n) not in brokens : # 해당 숫자가 누를 수 있는 숫자인 경우
                    check = True # check를 True로 바꿔줌
                else :
                    check = False # 아닐 경우 False로 바꿔준 후, break. 해당하는 수에 단 한 숫자라도 있을 시 False로 바뀐 후 break됨
                    break
            if check : # 버튼으로 누를 수 있는 숫자인 경우
                stop = True # while문 탈출 트리거
                ans=i+len(str(N+i*pm)) # i(검사한 수에서 처음 주어진 N을 뺀 값이 i이다.)와 검사한 수의 길이를 더하면 답이 된다.
                break
        if stop :
            break
        i += 1 # while문의 i를 1씩 증가시킨다.
    ans100 = (abs(N-100)) # 다만, 100에서 +와 -만으로 증가시키는 경우도 포함시켜준다.
    ans = ans100 if ans100 < ans else ans # ans와 ans100 중 작은 값을 출력한다.
    print(ans)
else : # 숫자 버튼이 모두 부서진 경우, 100에서 +와 -만으로 채널을 이동해야한다.
    print(abs(int(N)-100))
