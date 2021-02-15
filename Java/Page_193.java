class Parent{ // 부모 클래스 선언
    public void print(){ // print 메소드 생성
        System.out.println("one");
    }
}

class Child extends Parent{ // 부모클래스의 메소드를 상속받음
    public void print(){ // 상속받은 print 메소드를 오버라이딩 해서 새로 작성
        super.print(); // 기존의 부모 클래스의 메소드를 호출해줌
        System.out.println("two"); // System.out.println();
    }    
}

public class Page_193 {
    public static void main(String[] args){
        Child obj = new Child(); // Child() 클래스의 객체를 생성
        obj.print(); // print 메소드를 실행, 이때 super에 의한 부모클래스의 print 메소드와 자식클래스의 print 메소드가 순서로 출력된다.
    }
}
