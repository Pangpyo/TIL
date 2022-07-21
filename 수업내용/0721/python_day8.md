## 파이썬 응용/심화
### 추가 문법
* List comprehension : 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  * ` [<expression> for <변수> in <iterable> if <조건식>]`
* Dictionary comprehension :표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
  * ` {key : value for <변수> in <iterable> if <조건식>}`
* ` lambda [parameter]` : 표현식
  * 람다함수 : 표현식을 계산한 결과값을 반환하는 함수
  * 특징 : return문을 가질 수 없음, 간편 조건문 외 조건문이나 반복문 가질 수 없음
  * 장점 : 함수를 정의해서 사용하는 것보다 간결함
  * def를 사용할 수 없는 곳에서도 사용 가능
* filter
  * 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환
