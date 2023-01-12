# HTML, CSS

날짜: 2023년 1월 12일

# 웹의 기본 구조

HTML : 구조

CSS : 디자인

Javascript : 동작

## HTML

### Syntax

- HTML is
    - Hyper Text Markup Language
    - 프로그래밍 언어가 아닌 마크업 언어
    - Markup Tag의 집합
    - W3C에서 표준관리
- Element(요소) - Tag
    - content의 type을 지정
    - Element_name은 표준으로 정
- Attribute(속성)
    - 생략가능
    - Element의 속성 지정
    - atrribute_name과 value set을 표준으로 정의
        - 속성 이름과 값이 같을 때는 값을 생략 가능!
- Comments(주석)
    - <!---->
    - 브라우저에선표시되지않음
    - 더읽고이해하기쉬움

```html
<a>Naver</a> <!-- Tag -->
<a href="www.naver.com">Naver</a> <!-- Attribute -->
<!-- 이것이 주석 -->
```

- Block level element
    - 대부분 Inline 요소과 Text 요소를 포함
    - 일부 요소는 Block 요소를 포함
    - 새로운 행에 표시
    - Ex) : <div>, <p>, <h1>, <form>, <table>, <li>…
- Inline level element
    - 오직 Inline요소와 Text요소 만 포함
    - Text 처럼 취급됨
    - 새로운 행에 표시 되지 않음
    - Ex): <span>, <a>, <img>, <input>, <label>...
    

### Sections

- `<article>`
    - 문서의 독립적인 부분을 구성하는 섹션
    - 위젯 등 독립적인 아이템
    - 예: News, BlogPost, Article
    - article 요소를 중첩 할 경우 외부 article요소와 연관된 내용
- `<section>`
    - 일반적인 문서 또는 프로그램의 섹션
    - 제목으로 시작하는 컨텐츠의 의미적 그룹
- `<nav>`
    - 네비게이션 링크로 구성된 섹션
    - 다른 페이지 또는 동일페이지의 다른 섹션 연결
- `<aside>`
    - 문서의 주 내용과 관련성이 낮은 내용
    - 일반적으로 사이드바 형태로 표현
    - 예: 사이트링크, 광고, nav 요소 그룹
- `<footer>`
    - 꼬리말
    - 가장 가까운 선행하는 <section> 의footer
    - 작성자, 연관링크, 저작권등
    - <address>또는<nav>등의요소를포함

### Grouping

- `<pre>`
    - Preformatted text
    - Block level element
    - 공백문자와줄바꿈문자를보존
- `<ol>`
    - OrderedList
    - Block level element
    - Attributes
        - start =number
        - type={1|A |a| I|i }
- `<ul>`
    - UnorderedList
    - Blocklevel element
- `<li>`
    - List item
    - <ol>또는<ul>안에서하나의Item을표현
    - Attributes
        - value=number, only within<ol>

### Text Level

- `<a>`
    - Anchor
    - Hyper link to another page
    - Inline level element
    - Attributes
        - href=URL
        - target={_blank|_parent|_self|_top|framename}
        - herflang=language_code
- `<span>`
    - Inline level element
    - Grouping inline level elements
    - No visual changes
- `<img>`
    - Defines an image
    - Inline level element
    - Attributes
        - src=URL
        - alt=text,대체text
        - height=pixels or %
        - width=pixels or %
        - usemap=#map_name
            - 이미지를 부분별로 설정 할 수 있음
        - ismap=ismap
            - 클릭한 부분의 좌표를 서버로 전달 할 수 있음

### Embedded

- `<audio>`
    - Audio콘텐츠재생
    - Attributes
        - src=URL
        - autoplay=autoplay,자동재생여부
        - loop=loop,반복재생여부
        - controls= controls, control 표시 여부
        - preload ={auto|metadata|none}
- `<video>`
    - Video콘텐츠재생
    - Attributes
        - src=URL
        - autoplay=autoplay, 자동재생 여부
        - loop=loop,반복재생여부
        - controls=controls,control 표시 여부
        - preload =preload
        - poster= URL, 재생 이전에 표시될 이미지
        - audio=muted
        - width=pixels
        - height=pixels

### Forms

- `<form>`
    - Block level element
    - 사용자입력Data를Server로전송
    - Input요소를포함
    - Attributes
    - action=URL,HTTP Request URL
    - method={get|post },HTTP Request Method
    - target={_blank|_self|_parent|_top|frame_name},Result target
    - accept =MIME_Type
    - accept-charset=charset
    - enctype={text/plain| multipart/form-data| application/x-www-form-urlencoded}
    - name =form_name
- `<input>`
  
    - User input
    - Inline level element
    - Elementsfor user inputfields
    - Dependingon thetypeattribute
    - Attributes
        - type= { text | button| checkbox| radio |password| file|image| submit| reset |
        hidden }
        - name =name,HTTP Request parameter name
        - value=value,HTTP Request parameter value
        - disabled =disabled
        - alt=text,alternate text
        
        ![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled.png)
        
        - [https://caniuse.com/](https://caniuse.com/) : 내가 어떤 기능을 어떤 브라우저에서 사용 할 수 있는지

태그를 잘 사용해야 하는 이유 : 올바른 태그를 사용해야 봇이 페이지의 구조를 이해해서 검색엔진에 노출이 됨. 의미에 맞게끔 쓰도록 노력하자!

## CSS

- CascadingStyleSheets
- (x)HTMLElement(Markup)의시각적표현(Appearance)정의
- CSS Levels
    - CSS,EarliestDraftinMay, 1995
    - CSS Level1,W3C Official Recommendation in Dec, 1996
    - CSS Level2,W3C Official Recommendation in May, 1998
    - CSS Level3,Working Draft(Not yet Recommendation)
        - 대부분 CSS3사용
- 장점
    - 구조와표현의분리,Sementic Markup
    - File Size 감소
    - 효율적이고 정교한 디자인 제어
    - Browser 호환성에 대처 용이

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%201.png)

- CSS Syntax
    - Selector, Property, Value
    
    ![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%202.png)
    
    - 주석
    
    ```css
    /* 주석은 이렇게*/
    ```
    
- Selector(선택자)
    - 스타일을지정할대상요소를선택하는데사용하는패턴표기법
- Universal Selector

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%203.png)

- Type Selector

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%204.png)

- ID Selector

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%205.png)

- Class Selector

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%206.png)

- Attribute Selector

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%207.png)

- Descendant Selector (자손)

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%208.png)

- Child Selector (자식)

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%209.png)

- Link pseudo class (가상 클릭 선택자)

![Untitled](HTML,%20CSS%20ade2f8305a3f48db9a1e138f4bfa5180/Untitled%2010.png)