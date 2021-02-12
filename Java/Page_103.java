import java.util.*; // java.util 모든 헤더파일? import

public class Page_103 {
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<>(); // ArrayList 기본 사용 ArrayList<자료형> 배열리스트이름 = new ArrayList<객체파라미터>(용량);
        list.add("Hello");
        list.add("World");
        for (String li:list){
            System.out.println(li);
        }
    }
}

// ArrayList list = new ArrayList();//타입 미설정 Object로 선언된다.
// ArrayList<Student> members = new ArrayList<Student>();//타입설정 Student객체만 사용가능
// ArrayList<Integer> num = new ArrayList<Integer>();//타입설정 int타입만 사용가능
// ArrayList<Integer> num2 = new ArrayList<>();//new에서 타입 파라미터 생략가능
// ArrayList<Integer> num3 = new ArrayList<Integer>(10);//초기 용량(capacity)지정
// ArrayList<Integer> list2 = new ArrayList<Integer>(Arrays.asList(1,2,3));//생성시 값추가