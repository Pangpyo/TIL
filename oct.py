import random


postmembers = [
    ["선영", "다영"],
    ["호빈", "선교"],
    ["우열", "준환"],
    ["광표", "문경"],
    ["광진", "세빈"],
    ["호빈", "태극"],
    ["세빈", "준환"],
    ["우열", "문경"],
    ["광진", "선영"],
    ["호빈", "세빈"],
    ["광표", "재윤"],
    ["준환", "문경"],
    ["우열", "광진"],
    ["세빈", "은빈"],
    ["다영", "호빈"],
    ["재윤", "준환"],
    ["광표", "태극"],
    ["광진", "문경"],
    ["선영", "우열"],
    ["문경", "태극"],
    ["은빈", "준환"],
    ["다영", "세빈"],
    ["우열", "호빈"],
    ["광진", "광표"],
    ["선영", "재윤"],
    ["다영", "은빈"],
    ["광표", "세빈"],
    ["선영", "태극"],
    ["다겸", "준환"],
    ["문경", "호빈"],
    ["우열", "재윤"],
    ["은빈", "태극"],
    ["문경", "재윤"],
    ["선영", "호빈"],
    ["세빈", "우열"],
    ["광표", "다겸"],
    ["다영", "준환"],
    ["광표", "준환"],
    ["다겸", "태극"],
    ["은빈", "호빈"],
    ["다영", "우열"],
    ["문경", "세빈"],
]


for mem in postmembers:
    mem.sort()
while 1:
    nowmembers = []
    bp = True
    person = [
        "광표",
        "세빈",
        "태극",
        "호빈",
        "준환",
        "은빈",
        "다영",
        "우열",
        "문경",
        "다겸",
    ]
    for a in range(len(person) // 2):
        temps = []  # temps 비우기
        while len(temps) < 2:
            temp = random.choice(person)
            if temp not in temps:  # 랜덤추출값 중복 방지
                temps.append(temp)  # 값 tmeps에 추가
                person.remove(temp)  # person에서는 추출된 값 삭제
        temps.sort()
        if temps in postmembers:
            bp = False
            break
        nowmembers.append(temps)
    if bp:
        for a in range(5):
            print(f"{a+1}조: {nowmembers[a][0]} {nowmembers[a][1]}")
        break
