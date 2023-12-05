from math import ceil

def solution(fuel, powers, distances):
    answer = 0
    MAX_TIME = 1_000_000
    s, e = 0, MAX_TIME
    def get_minimum_fuel(time, power, distance) : # 근의 공식을 사용하여 사용해야하는 연료 최소값 구하기
        u = power
        l = -power*time
        r = ((power*time)**2 - 2*power*distance)**0.5
        x1 = -(l+r)/u
        try :
            return ceil(x1)
        except :
            return -1
    N = len(powers)
    while s <= e : # 시간을 매개변수로 두고 이분탐색
        m = (s+e)//2
        can_arrive = True # m초 안에 도착 가능한지
        total_fuel = 0
        for i in range(N) :
            need_fuel = get_minimum_fuel(m, powers[i], distances[i])
            if need_fuel == -1 :
                can_arrive = False # 도착 불가능한경우 False
                break
            total_fuel += need_fuel
        if not can_arrive or total_fuel > fuel :
            s = m + 1
        else :
            e = m - 1
            answer = m
    return answer