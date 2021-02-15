import java.util.*; // ArrayList 사용을 위한 라이브러리

class Person{ // 클래스 선언
    String name; // 변수
    String tel; // 변수

    public Person(String name, String tel){ // 클래스 내부에 public 함수 선언
        this.name = name; // name 설정
        this.tel = tel; // tel 설정
    }
}

public class Page_168 {
    public static void main(String[] args){
        ArrayList<Person> list = new ArrayList<Person>(); // class를 Person으로 가지는 ArrayList 객체 생성, 공간은 비어있다.
        list.add(new Person("Lee","010101010")); // list.add를 객체를 생성해서 추가한다.
        list.add(new Person("In","010101011")); // list.add를 객체를 생성해서 추가한다.
        list.add(new Person("Kyu","1020303")); // list.add를 객체를 생성해서 추가한다.

        for (Person object : list){ // list 내용을 하나하나 Person 클래스에서? object로 가져와서 출력한다.
            System.out.println(object); // System.out.println();
        }
    } 
}
