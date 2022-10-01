def binary_search(list, n):
    start = 0
    last = len(list) - 1
    while start <= last:
        mid = (start + last) // 2
        if list[mid] == n:
            return mid
        elif list[mid] > n:
            last = mid - 1
        else:
            start = mid + 1
    return -1


def solution(registered_list, new_id):
    if new_id not in registered_list:
        answer = new_id
    else:
        S = ""
        N = ""
        for c in new_id:
            if not c.isdecimal():
                S += c
            else:
                N += c
        N = 0 if N == "" else N
        same_ids = []
        l = len(S)
        N = int(N)
        for r_id in registered_list:
            if r_id[0:l] == S:
                if r_id[l::]:
                    if int(r_id[l::]) > N:
                        same_ids.append(int(r_id[l::]))
                else:
                    same_ids.append(0)
        same_ids.sort()
        while 1:
            N += 1
            if binary_search(same_ids, N) == -1:
                break
        answer = S + str(N)
    return answer


# 34분
