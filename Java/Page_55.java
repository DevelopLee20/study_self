public class Page_55 {
    public static void main(String args[]){
        int year = 2021; // int 형 정수 선언 후 초기화
        boolean isYear; // 불리언 형 자료형 true 와 false 만 있다.
        // %는 나머지 연산자
        isYear = (year % 4) == 0; // 참이라면 true 거짓이라면 false가 저장됨
        System.out.println(isYear); // System.out.println();
    }
}
