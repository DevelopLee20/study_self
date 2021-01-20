# 플루터 공부

> '|     |' 은 사용자 지정 변수를 의미함

---

## 메인 함수

```dart
// main.dart
void main(){
    runApp('|App Name|'());
}

class '|App Name|' extends StatelessWidget{
}
```

> |App Name| 은 class 명과 똑같이 사용한다.
>
> StatelessWidget은 위젯인데 상태를 저장하지 않음

---

## Stateless / Stateful

```dart
class MyApp extends StatelessWidget // 상태변화를 감지 하지 않음
class MyApp extends StatefulWidget // 상태변화를 감지함
```
