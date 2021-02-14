public class Page_140{
    private String name; // private 연산자를 사용해서 class 내부에서 사용가능하다.
    private int balance; // private 연산자를 사용해서 class 내부에서 사용가능하다.

    public String getName() { return name; } // public 연산자를 사용해서 class 외부에서 사용가능하다.
    public void setName(String name) { this.name = name; } // this.name은 내부에서 사용하는 name 이다. 그러므로 this.name에 String name를 저장한다.
    public int getBalance() { return balance; }
    public void setBalance(int balance) { this.balance = balance; }

    public static void main(String[] args){
        Page_140 obj = new Page_140(); // obj 라는 객체를 생성한다.
        obj.setName("Tom"); // obj 객체에 setName 함수를 사용한다.
        obj.setBalance(100000); // obj 객체에 setBalance 함수를 사용한다.
        System.out.println(obj.getName()+obj.getBalance()); // System.out.println();
    }
}