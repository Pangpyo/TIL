# Java Day 1

날짜: 2023년 1월 11일

## Java - Data type

- Primitive DataType
    - 기본적(일반적)인값을기억하는변수의type

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled.png)

- Automatic promotions(implicit Type Casting ) > 묵시적 형 변환
    - 작은크기의 타입은 큰 크기의 타입으로 자동으로 형변환된다.
    - 정수형은실수형으로자동형변환된다.
        - long var=100;
        - float fvar= var;
        - int kvar=‘A’ ;
- Explicit Type Casting > 명시적 형 변환
    - 큰크기의타입을작은크기의타입으로변경할경우
    - 실수형을정수형의타입으로변경할경우
    - identifier=(target_type)value;
        - float fvar= 100;
        - long var=(long)fvar;

## Java - Operators

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%201.png)

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%202.png)

- `||` (조건합) 연산자의 특징 : `|` (논리합)와는 다르게 앞에서 True면 뒤 연산은 실행하지 않는다(어차피 True이니까)

```java
a = 10;
b = 20;
System.out.println((a += 10) > 15 || (b -= 10) > 15);
System.out.println("a = " + a + ", b = " + b);
```

- a = 20, b = 20이 출력됨

## 조건문

### if

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%203.png)

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%204.png)

### switch

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%205.png)

- `switch` : case아래에 있는 구문 실행 후 default에 있는 구문 실행

## 반복문

### for

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%206.png)

- 1번 예시 : 1 2 4 3 순서로 실행
- 2번 예시 : 향상된 포문, 배열의 값들을 하나씩 출력

### while

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%207.png)

```java
private static void byFor() {
    int sum = 0;
    int cnt = 100;
    double avg = 0;
    Random rand = new Random();

    for (int i = 0; i < cnt; i++) {
        sum += rand.nextInt(6) + 1;
    }
    avg = 1.0 * sum / cnt;
    // avg를 double형으로 하고싶다. 하지만 sum과 cnt는 int이기에 1.0을 곱해 double로 만든다
    System.out.printf("sum: %d, avg: %f%n", sum, avg); // printf는 가변인자로 받기에 파라미터의 개수가 변할 수 있다
		// printf로 변수를 넣어 값을 출력

}

public static void byWhile() {
    int sum = 0;
    int cnt = 100;
    double avg = 0;
    Random rand = new Random();
    int i = 0;

    while (i < cnt) { // while문은 조건만 들어감
        sum += rand.nextInt(6) + 1;
        i++;
    }
    avg = 1.0 * sum / cnt;

    System.out.printf("sum: %d, avg: %f%n", sum, avg);
}
```

### for에서 label 사용

```java
package com.ssafy.startcamp.forwhile;

public class Label {
	/*
	 * 평상 시, label 사용은 권장하지 않음.
	 * 알고리즘 문제를 풀 때는 사용하면 유용함. (가지치기)
	 */
	public static void main(String[] args) {
		a:
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					if (j >= 5) {
						continue a;
					}
					System.out.println(i + " " + j);
				}
				System.out.println("for(j) end");
			}
	
		System.out.println("end of 'a' label");

		b:
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					if (j >= 5) {
						break b;
					}
					System.out.println(i + " " + j);
				}
			}
		
		System.out.println("end of 'b' label");
	}
}
```

### Array

```java
public class ArrayTest_01 {
	public static void main(String[] args) {
		// 숫자 6개를 저장
		int a1 = 1;
		int a2 = 2;
		int a3 = 3;
		int a4 = 4;
		int a5 = 5;
		int a6 = 6;
		
		// 배열
		int[] arr = new int[6]; // 
		arr[0] = 1;
		arr[1] = 2;
		arr[2] = 3;
		arr[3] = 4;
		arr[4] = 5;
		arr[5] = 6;
		
		// 반복문 활용
		for (int item : arr) {
			System.out.println(item);
		}
			
		
		
	}
}

import java.util.Arrays;
import java.util.Random;

public class ArrayTest_03 {
    public static void main(String[] args) {

        int N = 6;
        Random rand = new Random();
        // @@TODOBLOCK: 1~6까지의 random 정수 5개를 저장할 배열을 만들고 값을 저장하시오.
        int[] resultArray = new int[5];
        for (int i = 0; i < resultArray.length; i++) {
            resultArray[i] = rand.nextInt(N) + 1;
        }
        System.out.println(Arrays.toString(resultArray)); // 어레이를 반복문 없이 출력
        // @@END:
        
        // @@TODOBLOCK: 위 배열에 저장된 요소 중 짝수만 더해서 합을 출력하시오.
        int sum = 0;
        for (int i = 0; i < resultArray.length; i++) {
            if (resultArray[i] % 2 == 0) {
                sum += resultArray[i];
            }
        }
        System.out.printf("총 합은: %d%n", sum);
        // @@END:
    }
}

public class ArrayTest_06 {

    @SuppressWarnings("unused")
    public static void main(String[] args) {
        int[] ints = new int[3];
        ints[2] = 10;

        char[] chars = {'S', 'S', 'A', 'F', 'Y'}; // 선언과 동시에 초기화

        String[] strs = {"S", "S", "A", "F", "Y"};

        boolean[] bools;
//        bools = {true, false, false}; // 오류. 선언과 동시에 초기화 해야 오류가 뜨지 않음
    }
}

public class ArrayTest_09 {
    @SuppressWarnings("unused")
    public static void main(String[] args) {
        int[] scores = {90, 80, 100};

        // @@TODOINLINE: 95점을 추가로 관리하기 부적절한 코드는?
        //scores[3] = 95;                            // #1
        // 인덱스 초과
        //scores = new int[]{90, 80, 100, 95};       // #2

        //scores = {90, 80, 100, 95};                // #3
        // 초기화는 선언과 같이 해야한다
        //scores = Arrays.copyOf(scores, 5);         // #4
        // scores[3] = 95;
        
        //int[] scores2 = new int[4];                // #5
        //System.arraycopy(scores, 0, scores2, 0, scores.length);  array copy를 사용
        //scores2[3] = 95;
        
    }
}

import java.util.Arrays;

public class ArrayTest_12 {
    public static void main(String[] args) {
        int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3};

        // @@TODOBLOCK: 각 숫자가 몇 번 사용 되었는지 숫자별로 사용 횟수를 출력 하세요.
        // @@KEEP: 사용 안된 숫자는 0으로 출력 한다
        int[] used = new int[10];
        // 초기값은 0 그 이유는? 기본형은 데이터 타입 초기화 값이 정해져있다.int는 0
				// String은 null
        for (int num : intArray) {
            used[num]++;
        }

        System.out.println(Arrays.toString(used));
        // @@END:
    }
}
```

![Untitled](Java%20Day%201%20b0a9464444054237abf1d118e26d0b68/Untitled%208.png)

- 메모리
    - method 영역 arr라는 변수가 저장되고
    - heap 영역에 new 선언된 arr의 배열이 저장됨
- 

### 문자열

```java
// 문자열 순회
string.charAt(0)

// 부분 문자열
string.substring(start, end)

// 문자열이 동일한지
string.equals(nstring) // == 은 주소를 비교한다
```