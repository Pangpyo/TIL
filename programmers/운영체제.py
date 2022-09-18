from collections import deque
import heapq
def solution(program):
    result = [0]*11
    deq = deque(sorted(program, key = lambda x : x[1])) # program을 실행 시간순으로 정렬
    loading = []
    t = 0 # 진행시간
    pt = 0 # 현재 진행중인 프로그램이 완료되는 시간
    print(deq)
    while True :
        while 1 :
            if deq and deq[0][1] == t : # 현재 시간에 호출되는 프로그램들을 모두 로딩에 넣어준다
                heapq.heappush(loading, deq.popleft())
            else :
                break
        if pt == t and loading: # 현재 시간에 진행중인 프로그램이 없고, 로딩중인 프로그램이 있으면
            a, b, c = heapq.heappop(loading) # 해당 프로그램중 가장 우선순위가 높은 프로그램을 꺼내서
            pt += c # 진행중인 프로그램이 완료되는 시간을 입력해주고
            result[a] += t-b # 단계에 로딩 시간을 입력해준다.
        if not deq and not loading and pt == t: # 더 이상 진행시킬 프로그램이 없고 진행시간과 현재 진행중인 프로그램이 완료되는 시간이 같을 경우, 
            result[0] += t # 총 진행시간을 입력하고
            break # 프로그램 종료
        print(pt, t, a, b, c, loading)
        t += 1
    return result


program= [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]


print(solution(program))