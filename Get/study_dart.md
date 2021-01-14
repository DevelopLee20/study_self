# Dart 언어 기본 개념

## 주석 처리

```dart
// 단일 주석
/*
여러 주석
*/
```

---

## 세미콜론 표시

> C언어, Java언어와 같이 표시함

---

## 자료형

```dart
int a; // 정수
double b; // 실수
String c; // 문자열
bool d; // 참 거짓 판단
num e; // int,double 상위타입
```

> 이때 자동 형 변환은 지원하지 않는다.

---

## 타입 추론 자료형

```dart
var i = 10;
var d = 10.0;
var s = 'Hello';
var list = [1,2,3,4]
```

> 입력되는 값이 어떤 것이냐에 따라서 스스로가 자료형을 판단하도록 하는 데이터형
>
> 일반적으로 dart에서 사용하는 변수 선언 방식이다.

---

## 상수 final

```dart
final String s = 'Hello';
s = 'word'; // 에러발생
```

> 이때 상수로 선언되어서 값이 변할 수 없는 상태이기 때문에 다른 값이 대입될 수 없다.

---

## 산술 연산자

```dart
int a = 10;
int b = 20;

a+b // 더하기
a-b // 빼기
a*b // 곱하기
a/b // 나누기
a~/b // 몫
a%b // 나머지
```

---

## 논리 연산자

```dart
&& // 그리고
|| // 또는
== // 같다
! // 부정
!= // 다르다
```

---

## 형 변환 - as 키워드

```dart
var c = 30;
double d = c as int; // double -> int

var c = 30.5;
int d = c as int; // 오류 발생
```

> as 키워드는 더 상위개념으로 변환가능하다. 그래서 위와 다르게 아래에서는 오류가 발생한다.

---

## 함수 선언 방식

```dart
int function(int x){
    return x + 10;
}
```

> 함수는 C언어와 선언 방식이 같다고 생각하면 될 것 같다.

---

## print 함수

```dart
void main(){
    _name = '여울';
    _age = 10;
    print('$_name은 $_age살입니다.');
    print('$_name은 ${_name.length}글자압니다.');
    print('10년 후에는 ${_age + 10}살입니다.');
}
```

> print를 사용할 때 포멧팅은 $(함수명)을 이용한다.
>
> ${_name.length}처럼 함수를 사용해서 특정 값을 출력할 수 있다.
>
> $을 사용한 포메팅은 연산자의 사용 또한 가능하다.

---

## 메소드

```dart
class Class{
    bool isEven(int num_1){
        return % 2 == 0
    }
}

var P_Class = Class();

Print(P_Class.isEven(10));
```

> Class 라는 클래스의 객체를 P_Class에 생성한 후 'bool isEven(int num)' 함수에 '10'을 넣어서 결과값을 출력합니다.

---

## 익명 함수 - 이름없는 함수

```dart
(num_1){
    return num_1 % 2 == 0
};
```

---

## 람다 함수 - 람다식

```dart
(num_1) => num_1 % 2 == 0;
```

---

## 선택 매개변수

```dart
void some({String name, int age}){}

void main(){
    some(name:'인규',age=21);
    some(name:'인규');
    some(age:10);
    some();
}
```

> 선택 매개변수의 핵심은 함수 정의시의 매개변수에 있는 '{}'이다. 매개변수를 선택적으로 넣어서 사용 가능하다.

```dart
void some(String name, {int age}){}

void main(){
    some(name:'인규',age=21);
    some(name:'인규');
    some(age:10);
    some();
}
```

> 위와 같은 방식으로 함수가 정의 되어있을 경우 'int age' 값만 선택적으로 정의할 수 있다.

```dart
void some(String name, {int age = 21}){}

void main(){
    some(name:'인규',age=20);
    some(name:'인규');
    some(age:10);
    some();
}
```

> 위와 같은 방식으로 미리 값을 초기화 할 수 있다.

---

## if, else if, else

```dart
string text = 'Hello World';

if (text is int){
    print('int');
}
else if (text is double){
    print('double');
}
else{
    print('text');
}
```

---

## 삼항 연산

```dart
var today = rainy ? 'umbrella' : 'nothing';
```

> 'rainy'값이 참일때 'today'값은 'umbrella' 거짓일때 'nothing'값을 가진다.

### 스위치 케이스 부터 ppt 2, 28 부터
