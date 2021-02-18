void main(){ // main 함수 C언어 같은 역할
  checkVersion(); // checkVersion() 함수를 실행한다. 비동기로 실행되었기 때문에 모든 작업이 끝난 후 저장된 값을 출력한다.
  print('end process'); // 문장을 출력
}

Future checkVersion() async{ // async 비동기(비동기화) 키워드, Future = 비동기 함수, 단일 값, 여러 개면 Stream
  var version = await lookUpVersion(); // await 키워드 : 언제 끝날지 모르는 작업
  print(version); // version 변수의 비동기 실행을 함?
}

int lookUpVersion(){ // int 형 lookUpVersion 함수
  return 12; // 12를 리턴함
}

// 동기 방식 : 직렬처리
// 비동기 방식 : 병렬처리