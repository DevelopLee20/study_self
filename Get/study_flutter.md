# 플루터 공부

## 삼항연산자

```dart
var visibility = isPublic ? 'public' : 'private'; // Public 일 경우 public 출력, 아니면 private 출력
String plyerName(String name) => name ?? 'Guest'; // 입력받은 name 이 Guest와 같은가 비교한다.
```

---

```dart
printInteger(int aNumber){ // printInteger 메소드 생성 매개변수는 int aNumber 이다.
    print('The number is $aNumber.'); // print(); 출력시 $변수명 으로 한다.
}

main(){
    var number = 42; // var 형 변수 추론해서 알아서 자료형을 정한다.
    printInteger(number); // 함수 실행
}
```
