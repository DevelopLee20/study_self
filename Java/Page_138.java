class A{ // class A
    // private int a;
    int b;
    public int c;
}

public class Page_138 {
    public static void main(String[] args){
        A obj = new A();

        // obj.a = 10; // private 로 선언되었기 때문에 A class 에서만 사용된다.
        obj.b = 20; // 일반형이기 때문에 사용가능하다.
        obj.c = 30; // public 이기 때문에 모든 클래스에서 사용가능하다.
    }
}
