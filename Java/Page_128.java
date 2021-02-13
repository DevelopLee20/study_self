class Math{ // Math 라는 클래스 생성
    int add(int x, int y){ // 자료형 이름(매개 변수)
        return x + y; // return 값 지정
    }
}

public class Page_128{ // 메인 클래스
    public static void main(String[] args){ // public static void main(String[] args)
        int sum;
        Math obj = new Math(); // obj 라는 이름의 객체를 Math 클래스를 통해서 생성한다.
        sum = obj.add(2,3); // sum 라는 변수에 생성된 객체의 add 함수를 이용한다.
        System.out.println(sum); // System.out.println(sum);
        sum = obj.add(7,8); // sum 라는 변수에 생성된 obj 객체의 add 함수를 이용한다.
        System.out.println(sum); // System.out.println(sum);
    }
}