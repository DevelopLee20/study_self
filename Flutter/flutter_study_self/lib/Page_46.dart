void main(){ // main 함수
  printOne(); // 메소드 실행
  printTwo(); // 메소드 실행
  printThree(); // 메소드 실행
}

void printOne(){ // 메소드 선언
  print('One'); // print();
}

void printTwo() async{ // async 비동기 함수 선언 => 동기화를 하지 않아서 나중에 출력됨
  Future.delayed(Duration(seconds: 1),(){ // Future(비동기 출력문).delayed(Duration(seconds: 1)) => 1초간 기다려라.
  // await Future.delayed(Duration(secondes: 2)) => 언제 끝날지 모르는 함수 이므로 일단 멈춘다. 그리고 마지막에 진행됨
    print('Future!!'); // print();
  });
}


void printThree(){ // printThree 메소드 선언
  print('Three'); // print();
}