import java.util.*;

public class Page_75 {
    public static void main(String args[]){
        String month; // 문자열 변수

        Scanner sc = new Scanner(System.in); // Scanner 객체(인스턴스) 생성
        month = sc.next(); // 다음 단어를 받음 sc.nextLine(); 은 한 문장을 받음

        int a = 0; // 정수형 변수 선언

        switch (month){ // month의 값에 따라서 a의 값이 변경됨
            case "jan":
                a = 10;
                break;
            case "feb":
                a = 20;
                break;
        }
        System.out.println(month+a);
        sc.close(); // Scanner close
    }
}
