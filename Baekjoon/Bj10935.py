# 10935 BASE64 인코딩

def solution():
    S = input()
    bits = []
    base64_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

    for s in S:
        bits.append(bin(ord(s))[2::].zfill(8))

    bits = ''.join(bits)
    l = len(bits)
    remainder = l % 6
    if remainder:
        bits += '0' * (6 - remainder)
    def to_dec(bits):
        dec = 0
        for i, b in enumerate(reversed(bits)):
            if b == '1':
                dec += 1<<i
        return dec
    l = len(bits)
    answer = []
    for i in range(0, l, 6):
        answer.append(base64_table[to_dec(bits[i:i+6])])
    padding = len(answer)%4
    if padding:
        answer += '='*(4-padding)
    return ''.join(answer)

if __name__ == "__main__":
    print(solution())