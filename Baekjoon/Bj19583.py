# 19583 싸이버개강총회 S2

import sys

sys.stdin = open("input.txt")

S, E, Q = input().split()

sh, sm = map(int, S.split(":"))  # 시간을 시, 분으로 받은 뒤 분으로 전환
stime = sh * 60 + sm

eh, em = map(int, E.split(":"))
etime = eh * 60 + em

qh, qm = map(int, Q.split(":"))
qtime = qh * 60 + qm
dic = {}
for line in sys.stdin:  # 이후의 모든 입력들을 받음
    t, name = line.split()  # 입력을 한줄씩 시간, 이름을 받음
    h, m = map(int, t.split(":"))  # 시간을 분으로 바꿔줌
    time = h * 60 + m
    if time <= stime:  # 채팅 시간이 시작 시간 이전인 경유
        dic[name] = [1, 0]  # 딕셔너리에 추가, 벨류의 첫번째 인덱스 1값으로 지정
    elif (
        etime <= time <= qtime and name in dic
    ):  # 시간이 개강총회 끝시간과 스트리밍 끝 시간 사이인 경우, 또 시작 시간 이전 채팅 기록이 있을 경우
        dic[name][1] = 1  # 벨류의 두번째 인덱스를 1으로 지정
cnt = 0
for i, v in dic.items():  # 딕셔너리의 값을 뽑아옴
    if v[0] == 1 and v[1] == 1:  # 두 벨류값이 모두 1일 경우
        cnt += 1  # +1
print(cnt)  # 출력
