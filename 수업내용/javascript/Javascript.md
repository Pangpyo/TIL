# Javascript

날짜: 2023년 1월 13일

# Javascript

## Syntax

- 페이지의 동적인 동작을 위한 언어
- HTML 파일 내부에 `<script>`를 넣어 작성함
- URL주소(java script:)

```jsx
<html>
<head>
<script type="text/javascript" src="some/path/file.js">
</script> // 자바스크립트 파일을 불러온것
<script type="text/javascript">
	alert(‘hellojs’); // 자바스크립트를 작성
</script>
</head>
<body onload="alert('clicked')"> // 태그 내부에 작성
	<a href="javascript:alert('hello')">Click Me</a>
</body>
</html>
```

- Loosely Typed Language
    - 동적 타입 언어. 변수의 타입형을 지정하지 않음
- 주석
    - `//` or `/* */`\
- Naming Convention
    - 변수, 함수 : 소문자, 두번째 단어부터 첫글자 대분자
        - var hello, helloWorld
- 자바스크립트는 객체지향을 지원한다
    - ES6부터 객체지향 요소 추가
- 변수 선언
    - 선언부에 Datatype 기재 X
    - ‘var’로 변수 선언
    - 선언문이 위치한 영역에 따라 전역/지역변수 결정
- 함수 선언
    - 선언부에 Return Type을 기재 하지 않는다
    - ‘function’ 키워드 사용
    
    ```jsx
    <script type="text/javascript"> 
    function f(){
    	alert('function'); // 함수 선언
    }
    f();// 함수호출
    var f2 = function(){ // javascript는 일급 객체를 지원, 변수에 함수를 담을 수 있다
    	alert('function 2');
    }
    f2();//함수호출
    </script>
    ```
    

## Event

- 웹 페이지와 사용자의 인터렉션을 처리 할 수 있다

![Untitled](Javascript%200a5e4251b114497390cb59b181d22af0/Untitled.png)