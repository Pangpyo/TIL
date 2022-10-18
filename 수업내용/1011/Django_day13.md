## Foreign Key

### 개념

* 외래 키(외부 키) 
* 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키 
* 참조되는 테이블의 기본 키(Primary Key)를 가리킴 
* 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨 
  * 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음 
* 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
* 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성) 
  * 참조 무결성 : 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성 
    * 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 해당 테이블의 기본 키 값으로 존재 
* 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

## 1:N (Article - Comment)

### 모델 관계 설정

* 게시판의 게시글와 1:N 관계를 나타낼 수 있는 댓글 구현 
  * 1:N 관계에서 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될 것 
  * 게시글은 댓글을 0개 이상 가진다. 
    * 게시글(1)은 여러 개의 댓글(N)을 가진다. 
    * 게시글(1)은 댓글을 가지지 않을 수도 있다. ]
  * 댓글은 반드시 하나의 게시글에 속한다.

### Django Relationship fields 종류

* `OneToOneField() `
  * A one-to-one relationship 
* `ForeignKey() `
  * A one-to-many relationship 
* `ManyToManyField() `
  * A many-to-many relationship

### `ForeignKey(to, on_delete, **options)`

* A one-to-many relationship을 담당하는 Django의 모델 필드 클래스 
* Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당 
* 2개의 필수 위치 인자가 필요 
  * 참조하는 model class 
  * on_delete 옵션

### ForeignKey arguments - on_delete

* 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의 
* 데이터 무결성을 위해서 매우 중요한 설정 
* on_delete 옵션 값 
  * CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제 
  * PROTECT, SET_NULL, SET_DEFAULT … 등 여러 옵션 값들이 존재 
  * 수업에서는 CASCADE 값만 사용할 예정

### Comment 모델 정의

* 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작 성됨 
* ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자) 으로 작성하는 것을 권장 (이유는 이어지는 모델 참조에서 확인 예정)

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
def __str__(self):
	return self.content
```

## Comment 구현

### CREATE

```python
# articles/forms.py

from .models import Article, Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article',)
            
# articles/views.py
from .forms import ArticleForm, CommentForm
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
    	'article': article,
    	'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <form action="#" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
    </form>
{% endblock content %}
```

* 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까? 
* detail 페이지의 url을 살펴보면 path(‘/', views.detail, name='detail’) url에 해당 게시글의 pk 값이 사용 되고 있음 
* 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값 
* 이전에 학습했던 url을 통해 변수를 넘기는 variable routing을 사용

```python
# articles/urls.py
urlpatterns = [
    ...,
    path('<int:pk>/comments/', views.comments_create,
name='comments_create'),
]

# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # article 객체는 언제 저장할 수 있을까?
        comment_form.save()
    return redirect('articles:detail', article.pk)

<!-- articles/detail.html -->
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
	<input type="submit">
</form>
```

* 작성을 마치고 보면 article 객체를 저장하지 못함 
* 그래서 `save()` 메서드는 데이터베이스에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스 만을 반환해주는 옵션 값을 제공

### The save() method

* `save(commit=False)`
  * “Create, but don't save the new instance.” 
  * 아직 데이터베이스에 저장되지 않은 인스턴스를 반환 
  * 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
* save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기

```python
# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

### READ

* 작성한 댓글 목록 출력하기
* 특정 article에 있는 모든 댓글을 가져온 후 context에 추가

```python
# articles/views.py
from .models import Article, Comment

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

<!-- articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
...
<a href="{% url 'articles:index' %}">back</a>
<hr>
    <h4>댓글 목록</h4>
    <ul>
        {% for comment in comments %}
            <li>{{ comment.content }}</li>
        {% endfor %}
    </ul>
    <hr>
    ...
{% endblock content %}
```

### DELETE

```python
# articles/urls.py
urlpatterns = [
...,
path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

<!-- articles/detail.html -->
{% block content %}
...
<h4>댓글 목록</h4>
	<ul>
        {% for comment in comments %}
        <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
        </form>
        </li>
        {% endfor %}
    </ul>
<hr>
...
{% endblock content %}
```

## Comment 추가 사항

### 댓글 개수 출력하기

```python
<!-- DTL filter - length 사용 -->
{{ comments|length }}
{{ article.comment_set.all|length }}
<!-- Queryset API - count() 사용 -->
{{ comments.count }}
{{ article.comment_set.count }}

<!-- articles/detail.html -->
<h4>댓글 목록</h4>
{% if comments %}
    <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

### 댓글이 없는 경우 대체 컨텐츠 출력하기

```django
<!-- articles/detail.html -->
{% for comment in comments %}
    <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
        </form>
    </li>
{% empty %}
    <p>댓글이 없어요..</p>
{% endfor %}
```

