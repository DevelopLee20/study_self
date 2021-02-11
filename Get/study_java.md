# Java 언어 기본

## 자바 기본 클래스

```java
public class main{
    public static void main(String[] args){
        코드 내용
    }
}
```

---

## 문자 출력 방식

```java
System.out.println("Hello Java");
```

---

## 변수 선언 방식

```java
int number;
number = 10;
int number = 10;
```

---

## 자료형이 다른 변수끼리 연산

```java
short A = 10; // 2바이트 정수형
int B = 20; // 4바이트 정수형

System.out.println(A+B); // 결과값 30
```

### 정수형들은 연산시에 4바이트를 기본 단위로 사용하기 때문에 서로 다른 데이터형이어도 상관없다. 또한 저장되는 값 또한 정수형으로 저장된다

---

## 문자형 대입 방법

```java
char A = 'A';
char B = 66;

System.out.println(A); // 출력 : A
System.out.println(B); // 출력 : B
```

---

## 데이터형 변환 방법

```java
int A = 65;

System.out.println(A); // 출력 : 65
System.out.println((char)A); // 출력 : A
```

---

## 부동소수점 식별자

```java
double a = 3.14;
float b = 3.14F;
float c = 3.14f;

System.out.println(a); // 3.14
System.out.println(b); // 3.14
System.out.println(c); // 3.14
```

> 실수형은 기본적으로 double 형이다.  그래서 float 형을 선언해서 초기화 할때는 double 형이 아닌 float 형으로 선언하겠다는 F or f 식별자를 표시해주어야 한다

---

## 리스트, 배열의 길이

```python
#python
s = []
len(s)
```

```java
//java
int[] s = new int[10];
int[] score = {10,20,30,40};
s.length;
```

---

## 배열 인자 하나씩 호출

```python
#python
s = [1,2,3,4,5,6]
for i in s:
    print(s)
```

```java
//java
int[] s = {1,2,3,4,5};
for (int value : s){
    System.out.println(value+" ");
}
```

---

## 배열의 모든 요소 출력

```python
#python
s = [10,20,30]
print(s)
```

```java
//java
int[] s = {10,20,30};
System.out.println(Arrays.toString(number));
```

---

## 자바의 ArrayList = 파이썬의 list와 같다

```java
import java.util.*;

public class First_java{
    public static void main(String args[]) {
        ArrayList<String> list=new ArrayList<>();
        list.add("인규");
        list.add("감자");
        list.add("사과");
        for(String obj:list) {
            System.out.print(obj+" ");
        }
    }
}
```

---

## 객체지향언어

```java
class Calculator{

    int plus(int a,int b) {
        return a+b;
    }
    int minus(int a, int b) {
        return a-b;
    }
}

public class First_java{
    public static void main(String[] args) {
        Calculator obj1 = new Calculator();

        int one = obj1.plus(10, 20);
        int two = obj1.minus(30, 20);
        System.out.println(one);
        System.out.println(two);
    }
}
```

---

## String[] args 와 String args[] 의 차이점

```java
String[] args
String args[]
```

> <https://stackoverflow.com/questions/13175193/java-array-convention-string-args-vs-string-args>
>
> 결론적으론 없다.

---
