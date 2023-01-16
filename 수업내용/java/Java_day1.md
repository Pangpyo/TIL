# Java day1

날짜: 2023년 1월 16일

# JAVA day1

## JAVA 기본

### Variable(변수)란?

- 자료를 저장하기 위한 메모리 공간으로 타입에 따라 크기가 달라짐
- 메모리 공간에 값을 할당 후 사용

### Type(형)이란?

- 데이터의 종류
    - 기본형 : 미리 정해진 크기의 Memory사이즈로 표현 변수 자체가 값 저장
    - 참조형 : 크기가 미리 정해질 수 없는 데이터의 표현, 변수에는 실제 값을 참조할 수 있는 주소만 저장

### 기본형

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled.png)

- 파란색 변수형들은? : int, double은 기본형!
- byte는 8bit인데 왜 2^7까지만 처리하지? : 첫자리는 부호!
- int  범위 : 20억쯤
- float와 double의 가장 큰 차이는? : 유효자리의 수(정확성) double이 더 정확
- 범위를 벗어나면 overflow가 발생한다. 오버플로우는 오류가 아니니 주의할 것
    - int의 최대값인 2^31-1에서 1을 더하면 -2^31
- float, double같은 실수의 연산은 정확하지 않다
    - 유효 자리수를 이용한 반올림 처리를 하기 때문
    - 정수로 만들어서 연산하기
        - 다시 나눌 때 100.0 사용
    - `BigDecimal` 사용하기
- 형 변환이란?
    - 변수의 타입을 다른 타입으로 변환하는 것
    - privitive는 privitive끼리, reference는 reference끼리 형 변환 가능
        - boolean은 다른 기본 타입과 호환되지 않음
        - 기본 타입과 참조형의 형 변환을 위해서 Wrapper클래스 사용
            - Wrapper클래스 : Boolean, Interger, Double 등..
    - 형 변환 방법
        - 형 변환 연산자(괄호) 사용
            
            ```java
            double d = 100.5;
            int result = (int)d;
            ```
            
    - 기본형의 형 변환 진행
        - 묵시적 형 변환과 명시적 형 변환
            
            ```java
            // 묵시적 형 변환
            byte b = 10;
            int i = (int)b; //이것도 가능하지만
            int i2 = b; //이렇게 연산자 생략 가능!
            // 명시적 형 변환
            int i = 300;
            byte b = (byte)i; //연산자 생략 불가능
            ```
            
        
        ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%201.png)
        
        - 명시적 형 변환은 값 손실의 가능성이 있으므로 프로그래머가 직접 진행
        - 묵시적 형 변환은 자료 손실의 가능성이 없으므로 JVM이 진행해줌
        - 값의 크기, 타입의 크기가 아닌 타입의 표현 범위가 커지는 방향으로 할당할 경우에는 묵시적 형 변환 발생
        - short와 char가 묵시적 형 변환이 안되는 이유?
            - char는 0부터 시작한다.(음수 없음)

### 연산자란?

- 어떤 기능을 수행하는 기호
- 연산자의 종류와 우선순위 및 결합 방향

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%202.png)

- 연산자의 우선순위를 모두 알기는 힘들기 때문에, 괄호를 적절히 사용하자

```java
public static void main(String[] args) {
      byte b1 = 10;
      byte b2 = 20;
      byte b3 = b1 + b2;
      // 정수형 연산의 기본형은 int이기때문에 좌우의 타입이 맞지 않게된다.
      int i1 = 10;
      long l1 = 20;
      int i2 = i1 + l1; 
      // 위의 연산에서는 둘중 큰 타입으로 형 변환 후 진행되기 때문에 오류가 발생한다
      // TODO: 다음에서 발생하는 오류를 읽고 원인을 말한 후 수정하시오.
  }
```

- `||`, `|`
    - `||` 는 앞의 연산이 맞으면 뒤의 연산을 진행하지 않는다
    - `|`  는 뒤의 연산까지 진행한다

### 조건문

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%203.png)

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%204.png)

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%205.png)

### 배열

- 동일한 타입의 변수를 여러 개 사요ㅕㅇ하면
    - 변수의 개수 증가
    - 코드의 길이 증가
    - 반복문 적용 불가
    - 변수의 수가 동적으로 결정될 경우, 사용 불가
- 배열(Array)로 동일 타입 변수 묶어서 사용하기
    - 배열이란?
        - 동일한 타입의 데이터 0개 이상을 하나의 연속된 메모리 공간에서 관리하는 것
        - 요소에 접근하는 속도가 매우 빠르다
        - 한번 생성하면 크기 변경 불가
- Array 만들기 #1
    - `타입[] 변수명;` or `타입 변수명[];`
    - 변수의 타입과 저장하는 데이터의 타입?
        - `int a`, `int[] arr`
            - a의 타입? : 기본형 정수형
            - arr의 타입? : 참조형
            - arr이 저장하는 데이터의 타입? : 기본형 정수형
- 배열의 생성과 초기화
    - 생성
        - `new data_type[lenght]`
        - `point = new int [3]`
        - point는 메모리에 있는 배열을 가리키는 reference 타입 변수
    - 배열 요소의 초기화
        - 배열의 생성과 동시에 저장 대상 자료형에 대한 기본값으로 default 초기화 진행
        
        ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%206.png)
        
- 배열의 사용
    - 배열은 index번호를 가지고 각 요소에 접근 가능
        - index 번호는 0부터 시작
        - 배열의 길이 : `배열이름.length`로 배열의 크기 조회 가능
- Array 출력을 편리하게
    - `Arrays.toString()`
    - `arrays.toCharArray()`
- Array 만들기 #2
    - 생성과 동시에 할당한 값으로 초기화
        - `int [] b = new int [] {1, 3, 5, 6, 8};`
        - `int [] c = {1, 3, 5, 6, 8};`
    - 선언과 생성을 따로 처리할 경우 초기화 주의
- 배열의 생성과 메모리 사용 과정

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%207.png)

- for-each with Array
    - 가독성이 개선된 반복문으로,. 배열 및 Collections에서 사용
    - index대신 직접 요소에 접근하는 변수 제공
    
    ```java
    for( int x : intArray){
    	System.out.println(x);
    }
    ```
    
- Array is Immutable
    - 배열은 최초 메모리 할당 이후, 변경할 수 없음
    
    ```java
    int [] nums = {1, 2, 3};
    nums = new int[] {1, 2, 3, 4};
    nums[1] = 100;
    // nums는 배열일까? 아니다! nums는 배열을 가리키는 주소일 뿐
    ```
    
    - 개별 요소는 다른 값으로 변경이 가능하나, 요소를 추가하거나 삭제할 수는 없음
- 배열의 복사
- api에서 제공한는 배열 복사 method
    - `System.arrayCopy`
    - `Arrays.copyOf`

### 다차원 배열

- 2차원 Array 만들기 #1
    - int Type 기준으로 4x3 배열 만들기

![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%208.png)

- 2차원 Array 만들기 #2
    - int Type 기준으로 4x3 배열과 값을 동시에 만들기
    
    ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%209.png)
    
- 2차원 Array 만들기 #3
    - int Type 기준으로 4x? 배열 만들기
    
    ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%2010.png)
    
    - 1차 Array만 생성 후, 필요에 따라 2차 배열을 생성함
    
    ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%2011.png)
    
- 다차원 배열
    - 2차원 배열의 메모리 사용 단계
    
    ![Untitled](Java%20day1%2045923a1d793146c2be515e785790c174/Untitled%2012.png)
    
    - `arr3[1]` 에는 `arr2`, 2차원 배열이 들어가므로 `arr[1][1] = 100;` 은 불가능!
    - `arr[1][1]` 에는 `arr`가 들어가거나 `arr[1][1][1]`에 100이 들어가야한다

###