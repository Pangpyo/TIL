## 객체지향 프로그래밍이란?

* 파이썬은 모두 객체(object)로 이루어져 있다.
* 객체(object)는 특정 타입의 인스턴스(instance) 이다.

### 객체

* 객체(object)의 특징
  * 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  * 속성(attribute) : 어떤 상태(data)를 가지는가?
  * 조작법(method) : 어떤 행위를 할 수 있는가?
* 객체지향 프로그래밍이랑?
  * 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

* 예시 : 절차지향 프로그래밍

  * ```python
    def area(x, y) :
        return x*y
    def circumference(x, y) :
        return 2*(x+y)
    a=10
    b=30
    c=300
    d=20
    sq1_area = area(a,b)
    sq1_cir = circumference(a,b)
    sq2_area = area(c,d)
    sq2_cir = circumference(c,d)
    ```

* 예시 : 객체지향 프로그래밍

  * ```python
    clss Rectangle :
        def __init__(self, x, y) :
            self.x = x
            self.y = y
        def area(self) :
            return self.x * self.y
        def circumference(self) :
            return 2 * (self.x + self.y)
    
    r1 = Rectangle(10, 30)
    r1.area()
    r2.circumference()
    
    r2 = Rectangle(300, 20)
    r2.area()
    r2.circumference()
    
    ```

  * 사각형 - 클래스(class)
  * 각 사각형 (r1, r2) - 인스턴스(instance)
  * 사각형의 정보 = 속성(attribute)
  * 사각형의 행동/기능 - 메소드(method)

* 객체 지향의 장점 

  * 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨
  * 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점을 가짐

### OOP(Object-oriented programming) 기초

* 기본 문법

  * ```python
    #클래스 정의
    class MyClass :
    	pass
    #인스턴스 생성
    my_instance = Myclass()
    #메서드 호출
    my_instance.my_method()
    #속성
    my_instance.my_attribute()
    ```

  * 객체의 틀(class)을 가지고, 객체(instance)를 생성한다.

* 클래스와 인스턴스

  * 클래스 : 객체들의 분류(class)
  * 인스턴스 : 하나하나의 실체/예(instance)

* 속성

  * 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

* 메소드

  * 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)