# 객체지향 프로그래밍 2

날짜: 2023년 1월 18일

## 상속

### 객체지향 언어의 특징

- OOP is A P.I.E

![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled.png)

### 상속(Inheritance)

- 기존 클래스의 자산(멤버)을 자식 클래스에서 재사용하기 위한 것
    - 부모의 생성자와 초기화 블록은 상속하지 않는다
- 기존 클래스의 멤버를 물려받기 때문에 코드의 절감
    - 부모의 코드를 변경하면 모든 자식들에게도 적용 > 유지 보수성 향상
- 상속의 적용
    - extends 키워드 사용
    
    ![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%201.png)
    

### Object 클래스

- 모든 클래스의 조상 클래스
    - 별도의 extends 선언이 없는 클래스들은 extends Object 가 생략된 것
    - 따라서 모든 클래스에는 Object 크래스에 정의된 메서드가 있음

### 다양한 상속 관계

![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%202.png)

- 상속의 관계는 is a 관계라고 함
    - Person is a Object, SpiderMan is a Person
- Person과 Employee의 관계?
- Object와 Employee의 관계?
- Employee와 SpiderMan의 관계?

### 단일 상속 (Single Inheritance)

- 다중 상속의 경우 여러 클래스의 기능을 물려받을 수 있으나 관계가 매우 복잡해짐
    - 동일한 이름의 메서드가 두 부모에게 있다면 자식은 어떤 메서드를 쓸 것인가?
- 자바는 단일 상속만 지원!
    - 대신 interface와 포함관계(has a)로 단점 극복
    
    ![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%203.png)
    

### 포함 관계 (Interface, has a)

- 상속 이외에 클래스를 재활용 하는 방법
    - 2개 이상의 클래스에서 특성을 가져올 때 하나는 상속, 나머지는 멤버 변수로 처리
- 포함 관계의 UML 표현 : 실선
- Spider의 코드를 수정하면 SpiderMan에도 반영되므로 유지 보수성 확보

## 메서드 재정의

### 메서드 오버라이딩(overriding)

- 조상 클래스에 정의된 메서드를 자식 클래스에 적합하게 수정하는 것

![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%204.png)

- 오버라이딩의 조건
    - 메서드 이름이 같아야 한다
    - 매개변수의 개수, 타입, 순서가 같아야한다
    - 리턴 타입이 같아야 한다
    - 접근 제한자는 부모보다 범위가 넓거나 같아야 한다
    - 조상보다 더 큰 예외를 던질 수 없다

### Annotation

- 사전적 의미 : 주석
- 컴파일러, JVM, 프레임워크 등이 보는 주석
- 소스코드에 메타 데이터를 삽입하는 형태
    - 소스코드에 붙여놓은 라벨
    - 코드에 대한 정보 추가 > 소스 코드의 구조 변경, 환경 설정 정보 추가 등의 작업 진행
- JDK 1.5의 annotation의 예
- `@Deprecated`
    - 컴파일러에게 해당 메서드가 deprecated 되었다고 알려줌
    - 중요도가 떨어져 더 이상 사용되지 않고 앞으로는 사라지게 될
- `@Override`
    - 컴파일러에게 해당 메서드가 override 되었다고 알려줌
    - 선언시 반드시 super class에 선언 되어있는 메서드 여야 함
- `@SuppressWarnings`
    - 컴파일러에게 사소한 warning의 경우 신경쓰지 말라고 알려줌

### Object 클래스

- 가장 최상위 클래스로 모든 클래스의 조상
    - Object 멤버는 모든 클래스의 멤버
    
    ![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%205.png)
    

### `toString` 메서드

- 객체를 문자열로 변경하는 메서드
- 하지만 주소값 출력… 내용을 출력하려면 오버라이딩해야함

### `equals` 메서드

- 두 객체가 같은지를 비교하는 메서드
- 두 개의 레퍼런스 변수가 같은 객체를 가리키고 있는가?
- 우리가 비교할 것은 정말 객체의 주소 값인가?
    - 두 객체의 내용을 비교할 수 있도록 equals 메서드 재정의
- 객체의 주소 비교 : `==` 활용
- 객체의 내용 비교 : `equals` 활용

### `super` 키워드

- `this`를 통해 멤버에 접근했듯이 `super`를 통해 조상 클래스 멤버 접근
    - `super.`을 이용해 조상의 메소드 호출로 조상의 코드 재사용
- 변수의 scope
    - 사용된 위치에서 점점 확장해가며 처음 만난 선언부에 연결됨
    - method 내부 > 해당 클래스 멤버 변수 > 조상 클래스 멤버 변수
- `this()`가 해당 클래스의 다른 생성자를 호출하듯 `super()` 는 조상 클래스의 생성자 호출
    - 조상 클래스에 선언된 멤버들은 조상 클래스의 생성자에서 초기화가 이뤄지므로 이를 재활용
    - 자식 클래스에 선언된 멤버들만 자식 클래스 생성자에서 초기화
- `super()` 는 자식 클래스 생성자의 맨 첫 줄에서만 호출 가능
    - 즉 생성자의 첫 줄에만 `this()` 또는 `super()` 가 올 수 있다
- 명시적으로 `this()` 또는 `super()`를 호출하지 않는 경우 컴파일러가  `super()`삽입
    - 결론적으로 맨 상위의 Object까지 객체가 다 만들어지는 구조

### static method는 재정의 될까?

- static method는 재정의(overriding)되지 않고 hiding만 됨

## package와 import

### package

- PC의 많은 파일 관리 > 폴더 이용
    - 유사한 목적의 파일을 기준으로 작성
    - 이름은 의미 있는 이름으로, 계층적 접근
- 프로그램의 많은 클래스 > 패키지 이용
    - 패키지 이름은 의미 있는 이름으로 만들고, `.`를 통해 계층적 접근
    - 물리적으로 패키지는 클래스 파일을 담고 있는 디렉터리
    - package name + class name으로 클래스 구분 > fully qualified name
- package의 선언
    - `package package_name;`
    - 주석, 공백을 제외한 첫번째 문장에 하나의 패키지만 선언
    - 모든 클래스는 반드시 하나의 패키지에 속한다
        - 생략시 default package에 속하는데 가급적 사용하지 말자
- 일반적인 package naming 룰
    - 세상에 단 하나뿐인 이름 사용하자
    - `소속.프로젝트.용도`
    
    ![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%206.png)
    

### import

- 다른 패키지에 선언된 클래스를 사용하기 위한 키워드
    - 패키지와 클래스 선언 사이에 위치
    - 패키지와 달리 여러 번 선언 가능
- 선언 방법
    - `import 패키지명.클래스명;`
    - `import 패키지명.*;` : 해당 패키지 아래의 모든 클래스 import
        - 하위 패키지까지 import 하지는 않는다
    - ctrl + shift + O를 사용해 ide에서 자동 import 가능
- import 한 package의 클래스 이름이 동일하여 명확히 구분해야 할 때
    - 클래스 이름 앞에 전체 패키지 명을 입력
    - ex) `java.util.List list = new java.util.ArrayList();`
- default import package
    - `java.lang.*;`

### static import

- static member에 대한 import
    - 자주 사용되는 static member를 import, 잘 사용하지는 않는다.

### 일반적인 클래스 레이아웃

![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%207.png)

- static block : 프로그램이 처음 실행 될 때, 메모리에 한번 적재됨.
    - 객체 생성과 무관
- 초기화 블록 :
    - 객체가 생성 될 때 생성

## 제한자

### 제한자

- 클래스, 변수, 메서드 선언부에 함께 사용되어 부가적인 의미 부여
- 종류
    - 접근 제한자 : public, protected, (default = package), private
    - 그 외 제한자
        - static : 클래스 레벨의 요소 설정
        - final : 요소를 더 이상 수정할 수 없게 함
        - abstract : 추상 메서드 및 추상 클래스 작성
        - synchronized : 멀티스레드에서의 동기화 처리
- 하나의 대상에 여러 제한자를 조합 가능하나 접근 제한자는 하나만 사용 가능
- 순서는 무관하나, 일반적으로 접근 제한자를 맨 앞으로

### final

- 마지막, 더 이상 바뀔 수 없음
- 용도
    - final class - 더이상 확장 할 수 없음 : 상속 금지 > 오버라이드 방지
        - ex)이미 완벽한 클래스들 : String, Math…
    - final method - 더 이상 재정의 할 수 없음 : overriding 금지
    - final variable - 더 이상 값을 바꿀 수 없음
    - Blank final - 값이 할당되지 않은 멤버 변수
    - static final - 단지 final만 있으면 객체마다 갖는 값으로 공용성이 없음, 상수는 객체와 무관하게 모두가 공용하는 값

### 데이터 은닉과 보호(Encapsulation)

- 누군가 당신의 정보를 마음대로 바꾼다면?
    - 외부에서 변수가 접근 할 수 있기 때문에 정보가 보호되지 못함
- 대책은?
    - 변수는 private 접근으로 막기
    - 공개되는 메서드를 통한 접근 통로 마련 : setter / getter
        - 메서드에 정보 보호 로직 작성

```jsx
class UnbelievableUserInfo {

    private String name = "홍길동";
    private int account = 10000;
		// 마음대로 정보를 바꾸지 못하도록 private 접근자 사용

    // getter를 통해 정보에 접근
    public String getName() {
    	return this.name;
    }
    public int getAccount() {
    	return this.account;
    }
    //
    //setter를 통해 정보를 변경
    public void setName(String name) {
    	if (name != null) {
    		this.name = name;
    	}
    	else {
    		System.out.println("부적절한 name 할당 시도 무시 : " + name);
    	}
    	
    }
    public void setAccount(int account) {
    	if (account > 0) {
    		this.account = account;
    	}
    	else {
    		System.out.println("부적절한 account 할당 시도 무시 : " + account);
    	}
    	
    }
    //
}
```

### 객체의 생성 제어와 Singleton 디자인 패턴

- 객체의 생성을 제한해야 한다면?
    - 여러 개의 객체가 필요 없는 경우
        - 객체를 구별 할 필요가 없는 경우 = 수정 가능한 멤버 변수가 없고 기능만 있는 경우
        - 이런 객체를 stateless 한 객체라고 한다.
    - 객체를 계속 생성/삭제하는데 많은 비용이 들어서 재사용이 유리한 경우
- Singleton 디자인 패턴
    - 외부에서 생성자에 접근 금지 > 생성자의 접근 제한자를 private으로 설정
    - 내부에서는 private에 접근 가능하므로 직접 객체를 생성 > 멤버변수이므로 private 설정
    - 외부에서 private member에 접근 가능한 getter 생성 > setter는 불필요
    - 객체 없이 외부에서 접근할 수 있도록 getter와 변수에 static 추가
    - 외부에서는 언제나 getter를 통해서 객체를 참조하므로 하나의 객체 재사용

## 접근 제한자와 encapsulation

### 접근 제한자 (Access modifier)

- 멤버 등에 사용되며 해당 요소를 외부에서 사용할 수 있는지 설정

![Untitled](%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%E1%84%8C%E1%85%B5%E1%84%92%E1%85%A3%E1%86%BC%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%B5%E1%86%BC%202%202f509ed52bcd4b91b692b6c645c4c719/Untitled%208.png)

- method override 조건의 확인
    - 부모의 제한자 범위와 같거나 넓은 범위로만 사용 가능
    - ex) protected 를 public으로 override 할 수 있지만, private, default 로는 할 수 없음