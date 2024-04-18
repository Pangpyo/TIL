# 10936 BASE64 디코딩 

def solution():
    S = input()
    bits = []
    b64_to_bits = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63, '=':0}
    pad_cnt = 0
    for s in S:
        if s == '=':
            pad_cnt += 1
            continue
        bits.append(bin(b64_to_bits[s])[2::].zfill(6))
    bits = ''.join(bits)
    if pad_cnt:
        bits = bits[0:-pad_cnt*2]
    l = len(bits)
    answer = [chr(int(bits[i:i+8], 2)) for i in range(0, l, 8)]
    return ''.join(answer)

if __name__ == "__main__":
    print(solution())