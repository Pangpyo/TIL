from collections import defaultdict


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return 65536
    else:

        def convertstr(word):
            strdic = defaultdict(int)
            strset = set()
            for i in range(1, len(word)):
                tc = word[i - 1 : i + 1]
                if tc.isalpha():
                    strdic[tc] += 1
                    strset.add(tc)
            return strdic, strset

        strdic1, strset1 = convertstr(str1)
        strdic2, strset2 = convertstr(str2)

        unionstr = strset1 | strset2
        interstr = strset1 & strset2

        unionnum = 0
        for u in unionstr:
            unionnum += strdic1[u] + strdic2[u]
        internum = 0
        for i in interstr:
            internum += min(strdic1[i], strdic2[i])

        answer = int((internum / (unionnum - internum)) * 65536)
        return answer
