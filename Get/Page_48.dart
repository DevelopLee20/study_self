import 'dart:convert'; // json통신을 위한 라이브러리 임포트

void main(){ // 메인 함수
  // 타입 추론형 jsonString 변수는 '''의 전체 내용이 담긴다.
  var jsonString = '''
  [
    {"score": 40},
    {"score": 80}
  ]
  ''';
  var scores = jsonDecode(jsonString); // 타입추론형 scores 변수, json파일을 Decode 해준다. jsonDecode(json파일명);
  print(scores is List); // print(); 디코드 한 scores 변수에 담긴 값은 리스트 형으로 출력된다.
  var firstScore = scores[0]; // scores의 첫번째 값이 firstSCorer 에 저장된다.
  print(firstScore is Map); // 저장된 값은 Map 형식을 띄고 있다, Map은 딕셔너리와 비슷함
  print(firstScore['score'] == 40); // score 라는 key 값이 value로 40을 가지고 있다.
  // true true true
}