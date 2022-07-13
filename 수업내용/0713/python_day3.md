## 파이썬 함수

### 함수의 기초

* 특정한 기능을 하는 코드의 조각
* 특정명령을수행하는코드를매번다시작성하지않고, 필요시에만호출하여간편히사용

* 사용자 함수

  * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수 작성 가능

  * ```python
    def example(x, y) : #def를 통해 선언
        return x + y*2 # return을 통해 결과값 전달
    ```

### 함수의 입력과 결과값(Input, Output)

* return

  * 함수는 반드시 값을 하나만 return한다.
  * 함수는 return과 동시에 실행이 종료된다.

* parameter : 함수를 실행할 때 함수 내부에서 사용되는 식별자

* argument : 함수를 호출 할 때, 넣어주는 값

  * 정해지지 않은 갯수의 arguments는 parameter에 *를 붙이고 keyword arguments 는 **를 붙인다

  * ```python
    def example(x, y) : 
        return x + y
    	return x - y #return을 두번 사용하면 실행되지 않는다
    ```

  * ```python
    def example(x, y) : #x, y는 parameter
        return x + y,  x - y #return한번에 두가지 값 반환이 가능하다.
    a, b = [1, 6]
    print(example(a, b)) # a, b는 arguments
    
    ```

### 함수 응용

* map 

  * 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환

  * ```python
    n, m = map(int, input().split()) #문자형으로 입력받은 변수들 정수형으로 전환 
    ```