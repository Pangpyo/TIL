# Django CRUD

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

- 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt

requirements.txt 파일이 있을경우
$ pip install -r requirements.txt
```

### 3. Django project 생성

```
$ django-admin startproject <pjt name> .
# short cuts 설치한 경우
$ django sp <pjt name>
```

## 2. articles app

### 1. app 생성

```
$ django-admin startapp <app name> .
# short cuts 설치한 경우
$ django sa <pjt name>
```

### 2. app 등록

```python
#settings.py

INSTALLED_APPS = [
    "articles", # 앱 이름 추가
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```



### 3. 프로젝트 urls.py 설정

```python
# pjt > urls.py

from django.contrib import admin
from django.urls import path, include # include 추가

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("articles.urls")),
]
```

## 3. Model 정의 (DB 설계)

### 1. 클래스 정의

```python
# articles > models.py

from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. 마이그레이션 파일 생성

```
$ python manage.py makemigrations
```

### 3. DB 반영(`migrate`)

```
$ python manage.py migrate
```

## 4.0 사전 설정 및 페이지 생성

### 1.base templates 생성

```django
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, intial-scale=1.0">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
        crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <header></header>
    {% block content %}
    {% endblock %}
</body>
</html>
```

### 2. settings.py

``` python
# pjt > settings.py

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], # 베이스 템플릿 설정
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

### 3. app urls.py 설정

```python
from django.urls import path
from . import views
# 폴더 내에 있는 views를 import

# 앱 이름 등록
app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
]
```

### 4. views.py 설정

```python
def index(request):
    return render(request, "articles/index.html")
```

### 5. index 페이지 생성 및 create 링크

```python
{% extends 'base.html' %}

{% block content %}
<!-- base template 적용 '%} -->
<a href="{% url 'articles:create' %}">작성하기</a>
<!-- create로 이동 링크 생성 -->
{% endblock %}
```



## 4. CRUD 기능 구현

### 1. create

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

* urls.py

```python
# pjt > articles > urls.py

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
```

* views.py

```python
def create(request):
    return render(request, "articles/create.html")
```

* create.html

```django
<!-- articles/templates/articles/create.html -->

{% extends 'base.html' %}

{% block content %}
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit">
</form>
{% endblock %}
```

* forms.py 생성

```python
# articles/templates/articles.forms.py

from django import forms
from .models import Article


# ModelForm class 생성
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
```

* views.py

```python
articles/views.py

from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/new.html", context=context)
```

### 2. read

> DB에서 게시글을 가져와서, template에 전달

* views.py

```python
articles/views.py

def index(request):
    # DB에 있는 모든 데이터를 pk 값으로 내림차순하여
    articles = Article.objects.order_by("-pk")
	
    # articles라는 변수를 통해 context에 담음
    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)
```

* index.html

```django
{% extends 'base.html' %}

{% block content %}
<a href="{% url 'articles:create' %}">작성하기</a>
{% for article in articles %}
<!-- 제목과 생성일, 수정일 -->
<h3>{{ article.title }}</h3>
<p>{{article.created_at}} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
{% endblock %}
```

#### 2-1. detail read

> 특정한 글을 본다.

* index.html

```django

<a href="{% url 'articles:create' %}">작성하기</a>
{% for article in articles %}
<!-- title에 링크 생성 -->
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{article.created_at}} | {{ article.updated_at }}</p>
<hr>
```

* urls.py

```python
# pjt > articles > urls.py

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]
```

* views.py

```python
articles/views.py

def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

* detail.html

```django
<h1>{{ article.pk }}번 게시글</h1>
<h2>제목 : {{ article.title }}</h2>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>내용 : {{ article.content }} </p>
```

### 3. update

> 특정한 글을 수정한다.  => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

* detail.html

```django
<h1>{{ article.pk }}번 게시글</h1>
<h2>제목 : {{ article.title }}</h2>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>내용 : {{ article.content }} </p>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
<!-- 수정 버튼 생성 -->
```

* urls.py

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
]
```

* views.py

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)
```

* update.html

```django
<h1>글 수정하기</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="수정">
</form>
```

### 4. delete

> 특정한 글을 삭제한다.

* index.html

```django
<a href="{% url 'articles:create' %}">작성하기</a>
{% for article in articles %}
<!-- 제목과 생성일, 수정일 -->
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{article.created_at}} | {{ article.updated_at }}</p>
<a href="{% url 'articles:delete' article.pk %}">삭제</a>
<!-- 삭제 링크 추가 -->
<hr>
{% endfor %}
```

* urls.py

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
```

* views.py

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")
```

### 번외 

깃허브 업로드시 장고 시크릿키 분리하기

1. secrets.json 생성

   ```
   {
   	"SECRET_KEY": "<Your Django SECRET KEY>"
   }
   ```

2.  setting.py 설정

   ```python
   import os, json
   from django.core.exceptions import ImproperlyConfigured
   
   BASE_DIR = Path(__file__).resolve().parent.parent
   
   
   secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치
   
   with open(secret_file) as f:
       secrets = json.loads(f.read())
   
   def get_secret(setting):
       """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
       try:
           return secrets[setting]
       except KeyError:
           error_msg = "Set the {} environment variable".format(setting)
           raise ImproperlyConfigured(error_msg)
   
   
   SECRET_KEY = get_secret("SECRET_KEY")
   ```

3. gitignore 파일에 추가

   ```
   # .gitignore 파일
   
   secrets.json
   ```