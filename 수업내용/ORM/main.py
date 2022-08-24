import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

import datetime
directors_tables = [('봉준호', datetime.date(1993, 1, 1)), 
('김한민', datetime.date(1999, 1, 1)), 
('최동훈', datetime.date(2004, 1, 1)), 
('이정재', datetime.date(2022, 1, 1)), 
('이경규', datetime.date(1992, 1, 1)), 
('한재림', datetime.date(2005, 1, 1)), 
('Joseph Kosinski', datetime.date(1999, 1, 1)), 
('김철수', datetime.date(2022, 1, 1)), 
]
for n, d in directors_tables :
    director = Director()
    director.name = n
    director.debut = d
    director.country = 'KOR'
    director.save()

# 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

genres_table = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']
for g in genres_table :
    genre = Genre()
    genre.title = g
    genre.save()

# 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

direcs = Director.objects.all()

for direc in direcs :
    print(direc.name, direc.debut, direc.country)

# 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

direc = Director.objects.get(id = 1)
print(direc.name, direc.debut, direc.country)

# 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

direc = Director.objects.get(country = 'USA')

# 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

direc = Director.objects.get(name = 'Joseph Kosinski')
direc.country = 'USA'
direc.save()

# 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

direcs = Director.objects.get(country = 'KOR')
for direc in direcs :
    print(direc.name, direc.debut, direc.country)

# 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

direcs = Director.objects.filter(country = 'KOR')
for direc in direcs :
    print(direc.name, direc.debut, direc.country)


# 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

direc = Director.objects.get(name = '김철수')
direc.delete()