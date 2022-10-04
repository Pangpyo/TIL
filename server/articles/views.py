from django.shortcuts import render
import random

# Create your views here.


def index(request):
    context = {
        "name": "김광표",
        "img": "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",
    }
    return render(request, "articles/index.html", context)


def dinner(request):
    pick = random.choice(list(range(4)))
    foods = [
        "족발",
        "햄버거",
        "치킨",
        "초밥",
    ]
    imgs = [
        "https://static.hubzum.zumst.com/hubzum/2019/07/26/11/8291a05e16b14e9b91eedc7a4375c934_780x585.jpg",
        "https://img.hani.co.kr/imgdb/resize/2017/0709/149948783091_20170709.JPG",
        "https://img.khan.co.kr/news/2021/05/09/l_2021051001000864600073041.jpg",
        "https://gurunavi.com/ko/japanfoodie/article/sushi/img/sushi_01.jpg",
    ]
    context = {
        "pick": foods[pick],
        "foods": foods,
        "img": imgs[pick],
    }

    return render(request, "articles/dinner.html", context)


def lotto(request):
    nums = list(map(str, range(1, 46)))
    lottonums = []
    win = [3, 11, 15, 20, 35, 44]
    bonus = 10
    for _ in range(1, 6):
        picknums = random.sample(nums, 7)
        mainnums = sorted(picknums[0:6], key=lambda x: int(x))
        bonusnum = picknums[6]
        cnt = 0
        for n in mainnums:
            if int(n) in win:
                cnt += 1
        rank = ""
        if cnt == 6:
            rank = " 1등 : 10억원!!!!!"
        elif cnt == 5:
            if bonusnum == bonus:
                rank = " 2등 : 5000만원!!!"
            else:
                rank = " 3등 : 150만원!!"
        elif cnt == 4:
            rank = " 4등 50000원!"
        elif cnt == 3:
            rank = " 5등 5000원"
        else:
            rank = " 꽝.. 다음 기회에!"
        lottonums.append(" ".join(mainnums) + " + " + str(bonusnum) + rank)
    context = {"lottonums": lottonums}
    return render(request, "articles/lotto.html", context)


def isoddeven(request, number):
    if number % 2 == 0:
        answer = "짝수"
    else:
        answer = "홀수"
    context = {"number": number, "answer": answer}
    return render(request, "articles/isoddeven.html", context)


def calculator(request, num1, num2):
    context = {
        "num1": num1,
        "num2": num2,
        "plus": num1 + num2,
        "minus": num1 - num2,
        "product": num1 * num2,
        "division": num1 // num2,
    }
    return render(request, "articles/calculator.html", context)


def yourname(request):
    return render(request, "articles/yourname.html")


def MBTI(request):
    mbtis = [["I", "E"], ["N", "S"], ["T", "F"], ["P", "J"]]
    yourmbti = ""
    for mbti in mbtis:
        yourmbti += random.choice(mbti)
    mbtiname = {
        "ISTJ": "청렴결백 논리주의자",
        "ISFJ": "용감한 수호자",
        "INTJ": "용의주도한 전략가",
        "INFJ": "선의의 옹호자",
        "ISTP": "만능 재주꾼",
        "ISFP": "호기심 많은 예술가",
        "INFP": "열정적인 중재자",
        "INTP": "논리적인 사색가",
        "ESTP": "모험을 즐기는 사업가",
        "ESFP": "자유로운 영혼의 연예인",
        "ENFP": "재기발랄한 활동가",
        "ENTP": "논쟁을 즐기는 변론가",
        "ESTJ": "엄격한 관리자",
        "ESFJ": "사교적인 외교관",
        "ENFJ": "정의로운 사회운동가",
        "ENTJ": "대담한 통솔자",
    }
    context = {
        "name": request.GET.get("name"),
        "yourmbti": yourmbti,
        "mbtiname": mbtiname[yourmbti],
    }
    return render(request, "articles/MBTI.html", context)


def kipsum(request):
    return render(request, "articles/kipsum.html")


def kipsumpage(request):
    paragraphs = request.GET.get("paragraphs")
    words = request.GET.get("words")
    yourparas = []
    klipsum = [
        "아니",
        "근데",
        "이건",
        "저는",
        "그러나,",
        "것",
        "하다.",
        "있다.",
        "나",
        "수",
        "않다.",
        "우리",
        "고기",
        "보다.",
        "더",
        "좋다.",
        "그리고,",
        "이",
        "경우",
        "좀",
        "인간",
        "사실",
        "신체",
        "소금",
        "생활",
        "새롭다.",
        "무엇일까?",
        "네,",
        "당연하다",
        "이미",
        "사용하다.",
        "왜?",
        "무엇을?",
        "어째서?",
        "지방",
        "현실",
        "먼저",
        "당신은",
        "불법",
        "비밀",
        "아니오!",
        "있는걸까?",
        "싫어!",
    ]
    for _ in range(int(paragraphs)):
        yourpara = ""
        for _ in range(int(words)):
            yourpara += random.choice(klipsum) + " "
        yourparas.append(yourpara)
    context = {
        "yourparas": yourparas,
    }
    return render(request, "articles/kipsumpage.html", context)
