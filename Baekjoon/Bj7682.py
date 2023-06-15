# 7682 틱택토 G5

def solution() :
    def ttt() :
        temp = input()
        if temp == 'end' :
            return temp
        board = [[temp[i*3+j] for j in range(3)] for i in range(3)]
        ox = [0, 0]
        ox[0] = temp.count("O")
        ox[1] = temp.count("X")
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        def check(x, y) :
            cnt = 0
            for i in range(4) :
                px = x + dx[i]
                py = y + dy[i]
                nx = x + dx[i+4]
                ny = y + dy[i+4]
                if px >= 3 or px < 0 or py >= 3 or py < 0 :
                    continue
                if nx >= 3 or nx < 0 or ny >= 3 or ny < 0 :
                    continue
                if board[x][y] == board[nx][ny] == board[px][py] :
                    cnt += 1
            return cnt
        O = 0
        X = 0
        for i in range(3) :
            for j in range(3) :
                if board[i][j] == "O" :
                    O += check(i, j)
                elif board[i][j] == "X" :
                    X += check(i, j)
        ans = "invalid"
        if ox[0] + 1 == ox[1]  and not O and X :
            ans = "valid"
        elif ox[0] == ox[1] and O and not X :
            ans = "valid" 
        elif ox[0] == 4 and ox[1] == 5 and not O and not X :
            ans = "valid"
        return ans
    ans = []
    while 1 :
        temp = ttt()
        if temp == 'end' :
            break
        ans.append(temp)

    return ans
if __name__ == "__main__" :
    print(*solution(), sep="\n")