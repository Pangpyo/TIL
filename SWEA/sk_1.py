def solution(bakery_schedule, current_time, k):
    ch, cm = current_time.split(":")
    ct = int(ch) * 60 + int(cm)
    cnt = 0
    answer = -1
    for timen in bakery_schedule:
        time, n = timen.split()
        h, m = time.split(":")
        t = int(h) * 60 + int(m)
        if t < ct:
            continue
        cnt += int(n)
        if cnt >= k:
            answer = t - ct
            break
    return answer


print(solution(["09:05 10"]))
