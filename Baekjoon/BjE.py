# E gahui and sousenkyo 4

def solution() :
    v, k = map(int, input().split())
    answers = set()
    while v >= 1 :
        if  v+k not in answers :
            answers.add(v)
        v -= 1

    print(len(answers))
    answers = list(answers)
    answers.sort(reverse=True)

    return answers
    

if __name__ == "__main__" :
    print(*solution(), sep='\n')