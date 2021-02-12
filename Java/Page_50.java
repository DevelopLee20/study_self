import java.util.Scanner; // scanner 즉 scanf 기능을 사용하도록 하는 헤더파일?

public class Page_50 {
    public static void main(String args[]){
        // Scanner 이름 = newe Scanner(System.in);
        Scanner sc = new Scanner(System.in); // Scanner는 sc라는 이름을 가지고 new 연산자로 클래스의 객체(인스턴스)를 생성하도록 해준다.
        int x, y;

        x = sc.nextInt(); // scanner 타입을 Int 형으로 정한다.
        y = sc.nextInt(); // sc.nextInt(); int의 대소문자를 유의한다.
        // 문자열 nextLine(); 등등 존재

        System.out.println(x+y);

        sc.close(); // Scanner를 사용한 후에는 close를 통해서 닫아 주어야 한다. (안닫아도 되지만 닫는것을 권장한다)
    }
}
