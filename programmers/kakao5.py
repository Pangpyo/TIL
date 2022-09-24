

def solution(commands):
    table = [[0]*51 for _ in range(51)]
    answer = []
    for command in commands :
        com = command.split()
        print(com)
        if com[0] == 'UPDATE' :
            print(1)
            if len(com) == 4 :
                table[int(com[1])][int(com[2])] = com[3]
            else :
                for i in range(51) :
                    for j, v in enumerate(table[i]) :
                        if v == com[1] :
                            table[i][j] = com[2]
        elif com[0] == 'MERGE' :
            table[int(com[3])][int(com[4])] = table[int(com[1])][int(com[2])]

        # elif com[0] == 'UNMERGE' :
        #     v = table[com[1]][com[2]]
        #     i = 1
        #     while 1 :
        elif com[0] == 'PRINT' :
            answer.append(table[int(com[1])][int(com[2])])     
    answer = []
    return answer