# 2290 LCD Test S2

def solution() :
    s, n = input().split()
    s = int(s)
    ans = []
    nums = [[1, 3, 0, 3, 1],
             [0, 2, 0, 2, 0],
             [1, 2, 1, 1, 1],
             [1, 2, 1, 2, 1],
             [0, 3, 1, 2, 0],
             [1, 1, 1, 2, 1],
             [1, 1, 1, 3, 1],
             [1, 2, 0, 2, 0],
             [1, 3, 1, 3, 1],
             [1, 3, 1, 2, 1]]
    wStick = [" ", "-"]
    lStick = [[" ", "|", " ", "|"], [" ", " ", "|", "|"]]
    for i in range(5) :
        temp = ""
        for number in n :
            number = int(number)
            if not i%2 :
                temp += " "
                temp += wStick[nums[number][i]]*s
                temp += " "
            else :
                temp += lStick[0][nums[number][i]]
                temp += " "*s
                temp += lStick[1][nums[number][i]]
            temp += " "
        if i%2 :
            for i in range(s) :
                ans.append(temp)
        else :
            ans.append(temp)

    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")