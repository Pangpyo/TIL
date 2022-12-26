# 2343 기타레슨 S1


N, M = map(int, input().split())

lecs = list(map(int, input().split()))


start = max(lecs)  # 블루레이의 크기는 최소한 가장 긴 강의보다는 커야한다
end = sum(lecs) // M + sum(lecs) // N  # 블루레이의 크기는 이 이상일 수 없다
ans = 0


while start <= end:  # 시작범위와 끝 범위가 같아질때까지
    mid = (start + end) // 2  # 블루레이의 용량
    temp = 0  # 첫 블루레이에 들어갈 강의의 길이
    cnt = 1  # 사용되는 블루레이의 개수
    for lec in lecs:
        if temp + lec <= mid:  # 강의를 블루레이에 넣어도 용량을 넘지 않는 경우
            temp += lec  # 강의를 현재 블루레이에 넣는다
        else:  # 넘는 경우
            cnt += 1  # 블루레이를 하나 더 꺼내서
            temp = lec  # 블루레이에 새 강의를 넣어준다
    if cnt > M:  # 사용되는 블루레이의 개수가 M보다 많은 경우
        start = mid + 1  # 시작 범위를 늘려 다시 탐색한다
    else:  # 더 적은 경우
        end = mid - 1  # 끝 범위를 줄여 다시 탐색한다
        ans = mid  # 그 중 최소값을 찾아야하므로 mid로 줄여간다


print(ans)
