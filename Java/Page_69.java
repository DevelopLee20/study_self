import java.util.Scanner;

public class Page_69 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in); // Scanner를 sc에 설정
        int number1 = sc.nextInt(); // 정수를 입력받음
        int number2 = sc.nextInt(); // 정수를 입력받음

        if (number1 < 0){ // 첫번재 조건문
            System.out.println("1");
        }
        else if (number2 > 0){ // 두번째 조건문
            System.out.println("2");
        }
        else{ // 나머지들
            System.out.println("3");
        }
        sc.close(); // Scanner close
    }
}
