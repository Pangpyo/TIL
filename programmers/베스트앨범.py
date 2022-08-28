# 해시>베스트 앨범



genres = ["R&B", "classic", "classic", "classic", "pop", "hiphop", "hiphop", "R&B", "R&B"]
plays = [900, 498, 500, 500, 800, 3000, 50, 900, 907]

def solution(genres, plays):
    dic = {}
    for i in range(len(genres)) :
        if genres[i] not in dic :
            dic[genres[i]] = [plays[i], [(i, plays[i])]]
        else :
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append((i, plays[i]))
    print(dic)
    dic = sorted(dic.items(), key = lambda x : -x[1][0]) # 장르별 재생 수가 많은 순으로 정렬
    print(dic)
    answer = []
    for i in dic :
        music = sorted(i[1][1], key = lambda x : (x[1], -x[0])) # 각 장르별로 재생순, 고유번호 역순으로 정렬
        print(music)
        for j in range(2) :
            ans = music.pop() # 재생수가 가장 많은 고유번호 2개를 뽑아옴
            answer.append(ans[0]) # 만약 장르에 한 곡만 있을 경우 1곡만 뽑아옴
            if not music :
                break
    return answer

print(solution(genres, plays))