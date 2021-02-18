void main() async{ // async 비동기 함수
  await getVersionName().then((value) => { // 비동기 함수 내에서 반환하는 값을 처리하기 위해서 then() 함수를 이용함
    print(value) // print()
  }); // then 함수는 여기까지 
  print('end process'); // print();
}

Future<String> getVersionName() async{ // Future 클래스 이므로 비동기 이며, 반환값을 <String>으로 지정한다. async 비동기 함수.
  var versionName = await lookUpVersionName(); // var 추론 데이터형, await 결과값이 필요하기 때문에 지정.
  return versionName; // String 반환함
}

String lookUpVersionName(){ // 메소드 선언
  return 'Android Q'; // String을 반환함
}