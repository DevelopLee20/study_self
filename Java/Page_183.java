class Animal{ // 부모 클래스가 될 Animal 클래스
    void eat(){
        System.out.println("eating...");
    }
}

class Dog extends Animal{ // 자식 클래스가 될 Dog 클래스
    void bark(){
        System.out.println("barking...");
    }
}

public class Page_183{
    public static void main(String[] args){
        Dog d = new Dog(); // Dog 클래스의 객체 생성
        d.bark(); // Dog 클래스의 메소드 bark() 사용
        d.eat(); // Dog 클래스에는 없지만 부모 클래스에 있는 eat() 메소드를 Dog 객체로 사용가능하다.
    }
}