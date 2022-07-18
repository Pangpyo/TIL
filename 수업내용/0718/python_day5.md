## 에러/ 예외 처리
### 디버깅
* ` print` 함수 활용
* 개발 환경에서 제공하는 기능 활용
* Python tutor 활용
* 뇌컴파일, 눈디버깅

### 에러와 예외
* 문법에러(Syntax Error)
  * 파이썬 프로그램이 실행되지 않음
  * 에러가 발생한 위치 표현
* 예외
  * 예상치 못한 상황을 맞이하면 프로그램 실행이 멈춤
  * 실행 중에 감지되는 에러들을 예외라고 부름
  * 사용자 정의 예외를 만들어 관리 가능
    * ZeroDivisionError : 0 으로 나누고자 할 때 발생
    * NameError : namespace 상에 이름이 없는 경우
    * TypeError : 타입 불일치, arguments 부족, 초과
    * ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
  

### 예외 처리

* try, except 를 이용하여 예외 처리를 할 수 있음

* try문

  * 오류가 발생할 가능성이 있는 코드를 실행
  * 예외가 발생되지 않으면, except 없이 실행 종료

* except문

  * 예외가 발생하면 except 절이 실행
  * 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

  ```python
  try
  	#try 명령문
  except #예외그룹 1 as 변수 1
  	#예외처리 명령문 1
  except #예외그룹 2 as 변수 2
  	#예외처리 명령문 2
  finally:
  	#finally 명령문
  ```

  

### 예외 발생 시키기

* raise를 통해 예외를 강제로 발생
  * ` raise <표현식>(메시지)`