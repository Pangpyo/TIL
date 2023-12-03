# D 가희와 클럽 오디션 1

def solution() :
    lv, hit = input().split()
    lv = int(lv)
    dic = {"miss" : 0, "bad" : 200*lv, "cool" : 400*lv, "great" : 600*lv, "perfect" : 1000*lv}

    return dic[hit]
    

if __name__ == "__main__" :
    print(solution())