# 5622 다이얼 B2

word = input()

sec = 0

for i in word :
    if i in ['A', 'B', 'C'] :
        sec += 3
    elif i in ['D', 'E', 'F'] :
        sec += 4
    elif i in ['G', 'H', 'I'] :
        sec += 5
    elif i in ['J', 'K', 'L'] :
        sec += 6
    elif i in ['M', 'N', 'O'] :
        sec += 7
    elif i in ['P', 'Q', 'R', 'S'] :
        sec += 8
    elif i in ['T', 'U', 'V'] :
        sec += 9
    else :
        sec += 10

print(sec)