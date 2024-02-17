def solution(arr) :
    answer = []
    TEN = 10
    def to_bit(leds) :
        bit = 0
        for led in leds :
            bit += 2**(ord(led)-ord("A"))
        return bit
    need_led = [0]*TEN
    need_led[0] = to_bit(("A", "B", "C", "D", "E", "F"))
    need_led[1] = to_bit(("B", "C"))
    need_led[2] = to_bit(("A", "B", "D", "E", "G"))
    need_led[3] = to_bit(("A", "B", "C", "D", "G"))
    need_led[4] = to_bit(("B", "C", "F", "G"))
    need_led[5] = to_bit(("A", "C", "D", "F", "G"))
    need_led[6] = to_bit(("A", "B", "D", "F", "G"))
    need_led[7] = to_bit(("A", "B", "C", "F"))
    need_led[8] = to_bit(("A", "B", "C", "D", "E", "F", "G"))
    need_led[9] = to_bit(("A", "B", "C", "D", "F", "G"))
    def count_bit(n) :
        cnt = 0
        for i in range(TEN) :
            if n & (1<<i) :
                cnt += 1
        return cnt
    MAX_BIT = 2**7 - 1
    for numbers in arr :
        number_exist = [False]*TEN
        union = 0
        inter = MAX_BIT
        for number in numbers :
            number_exist[int(number)] = True
        for i in range(TEN) :
            if number_exist[i] :
                union |= need_led[i]
                inter &= need_led[i]
        diff_led = count_bit(union)
        same_led = count_bit(inter)
        diff_button = diff_led-same_led
        same_button = 1 if same_led else 0
        answer.append(diff_button+same_button)
    return answer
print(solution(["29471500", "6813427", "0123456789"]))