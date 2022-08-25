# 2630 색종이 만들기 S2

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
black = 0
def cut(graph) :
    global white
    global black
    check = 0
    l = len(graph)
    if l > 1 :
        for i in range(l) :
            for j in range(l) :
                if graph[i][j] == graph[0][0] :
                    pass
                else :
                    check = 1
                    break

    if check == 1 : 
        ngraph = []
        x = [0, 0, l//2, l//2]
        y = [0, l//2, 0, l//2]
        for d in range(4) :
            mgraph = [[0]*(l//2) for _ in range(l//2)]
            for i in range(l//2) :
                for j in range(l//2) :
                    mgraph[i][j] = graph[i+x[d]][j+y[d]]
            ngraph.append(mgraph)
        
        for p in ngraph :
            cut(p)
    else :
        if graph[0][0] == 0 :
            white += 1
        else :
            black += 1

cut(paper)
print(white, black)