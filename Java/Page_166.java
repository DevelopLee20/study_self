import java.util.Scanner; // Scanner를 사용하기 위한 헤더파일

class Movie{ // Movie class
    String title, director; // 변수 선언
    public Movie(String title, String director){ // 모든 class 에서 사용하도록 public으로 선언
        this.title = title; // title 변수 설정
        this.director = director; // director 변수 설정
    }
}

public class Page_166 { // 파일명과 같게 설정
    public static void main(String[] args){ // public static void main(String[] args)
        Scanner sc = new Scanner(System.in); // sc를 Scanner객체 생성

        Movie [] list = new Movie[2]; // Movie 클래스의 객체 배열 생성, 배열의 크기는 2

        for ( int i = 0; i < list.length; i++){ // list의 길이만큼 반복
            System.out.print("title: "); // print 라인출력이 아닌 단일 출력
            String title = sc.nextLine(); // 다음 문자열을 받음
            System.out.print("director: "); // print 라인출력이 아닌 단일 출력
            String director = sc.nextLine(); // 다음 문자열을 받음
            list[i] = new Movie(title, director); // i번째 list에 변수를 대입해 생성한 객체를 저장한다.
        }
        sc.close();
    }
}
