# 2630 색종이 만들기 S2

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
white = 0  # 흰 종이의 총 개수
black = 0  # 파란 종이의 총 개수


def cut(graph):
    global white
    global black
    check = 0  # 자를수 있는지 없는지 확인
    l = len(graph)
    if l > 1:
        for i in range(l):
            for j in range(l):
                if graph[i][j] == graph[0][0]:  # 종이 전체가 같은 색이면 패스한다.
                    pass
                else:  # 아닌 경우 자른다
                    check = 1
                    break

    if check == 1:
        ngraph = []  # 잘려진 새로운 종이가 들어갈 리스트
        x = [0, 0, l // 2, l // 2]  # 4개의 구간으로 나눈다
        y = [0, l // 2, 0, l // 2]
        for d in range(4):
            mgraph = [[0] * (l // 2) for _ in range(l // 2)]  # 잘려진 새로운 종이
            for i in range(l // 2):
                for j in range(l // 2):
                    mgraph[i][j] = graph[i + x[d]][j + y[d]]  # 종이들의 색 정보를 입력한다
            ngraph.append(mgraph)  # ngraph안에 새로운 종이들이 4개 들어간다

        for p in ngraph:  # 각 종이별로 다시 cut을 진행한다
            cut(p)
    else:
        if graph[0][0] == 0:
            white += 1  # 종이 개수를 세어준다
        else:
            black += 1


cut(paper)
print(white, black)
