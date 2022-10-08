import random

person = [
    "김광표",
    "권세빈",
    "이태극",
    "이호빈",
    "김준환",
    "문재윤",
    "박선영",
    "여다영",
    "이우열",
    "이은진",
    "이광진",
    "김문경",
]

members_num = int(input("각 팀당 인원:"))
for a in range(len(person) // members_num):
    temps = []  # temps 비우기
    while len(temps) < members_num:
        temp = random.choice(person)

        if temp not in temps:  # 랜덤추출값 중복 방지
            temps.append(temp)  # 값 tmeps에 추가
            person.remove(temp)  # person에서는 추출된 값 삭제
    print(f"{a+1}조:{temps}")  # 1조부터 시작
