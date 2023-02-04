from heapq import heappop, heappush


def solution(companies, applicants):

    coms = {}
    names = []
    for com in companies:
        name, likes, cnt = com.split()
        coms[name] = [likes, int(cnt), []]
    apps = {}
    for app in applicants:
        name, likes, cnt = app.split()
        apps[name] = [likes, int(cnt), set()]
        names.append(name)
    comin = set()
    flag = True
    while flag:
        for name in names:
            if not apps[name][1] or name in comin:
                continue
            for ac in apps[name][0]:
                if ac in apps[name][2]:
                    continue
                heappush(coms[ac][2], (-coms[ac][0].index(name), name))
                comin.add(name)
                apps[name][1] -= 1
                if len(coms[ac][2]) > coms[ac][1]:

                    comin.remove(heappop(coms[ac][2])[1])
                apps[name][2].add(ac)
                break
        flag = False
        for name in names:
            if not apps[name][1] or name in comin:
                continue
            flag = True
    print(coms)
    print(apps)
    answer = []
    for com, result in coms.items():
        capps = []
        for capp in result[2]:
            capps.append(capp[1])
        capps = "".join(sorted(capps))
        answer.append("".join([com, "_", capps]))

    return answer


c = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
a = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]


print(solution(c, a))
