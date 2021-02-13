class Mymath{
    int square(int i){ // square 라는 메소드 생성
        return i * i;
    }

    double square(double i){ // square 라는 메소드를 중복 생성, 이때 매개변수는 다르게 설정해야한다.
        return i * i;
    }

    int square(){
        return 30 * 30;
    }
}

public class Page_130 { // 파일명과 같게 설정
    public static void main(String[] args){ // public static void main(String[] args)
        Mymath obj = new Mymath(); // Mymath 클래스에서 obj 라는 이름의 객체를 생성한다. new 연산자를 통한 인스턴스(객체) 생성
        // 메소드 오버리딩(오버라이딩) 동일한 이름의 메소드를 여러 개 정의하는 것이다.
        System.out.println(obj.square(10)); // System.out.println();
        System.out.println(obj.square(3.14)); // System.out.println();
        System.out.println(obj.square());
        // 매개변수에 맞는 메소드가 호출되어 사용된다.
    }
}
