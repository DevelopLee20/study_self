import java.util.ArrayList; // 배열리스트 사용하기 위한 헤더파일? 임포트

public class Page_167 {
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<String>(); // String 타입의 배열리스트의 이름을 list로 설정후 String 타입으로 객체를 생성한다. ()이므로 내용은 없다.
        list.add("one"); // list add "one"
        list.add("two"); // list add "two"

        System.out.println("system"); // System.out.println();
        int index = (int) (Math.random()*list.size()); // index 라는 변수는 list.size에서 랜덤으로 출력되어서 int형으로 저장된다.
        System.out.println(list.get(index)); // list.get(인덱스) 위치의 내용을 가져온다.
    }
}
