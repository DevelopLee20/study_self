class Animal{
    public void eat(){ // eat() 메소드
        System.out.println("eating...");
    }
};

class Dog extends Animal {
    public void eat(){ // Animal 클래스에서 상속받았지만 메소드를 재정의 한다. (메소드 오버리딩(오버라이딩))
        System.out.println("Dog eating...");
    }
};

public class Page_191{
    public static void main(String[] args){
        Dog d = new Dog(); // Dog 클래스의 객체를 생성한다.
        d.eat(); // 오버라이딩된 eat() 메소드를 사용한다.
    }
};