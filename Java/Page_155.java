class Pizza{
    private String toppings; // class 내부에서만 사용가능한 변수
    static int count = 0; // 정적 변수 static 모든 곳에서 사용된다.

    public Pizza(String toppings){ // class의 이름과 같게 설정
        this.toppings = toppings; // this.toppings 변수, toppings 는 String toppings
        count++; // count = count + 1;
    }
}

public class Page_155 {
    public static void main(String[] args){
        Pizza p1 = new Pizza("Super"); // Pizza라는 클래스에서 p1이라는 이름의 객체를 생성하고 Pizza 함수(인스턴스?)에 "Super"를 대입한다.
        Pizza p2 = new Pizza("Two"); // Pizza라는 클래스에서 p2라는 이름의 객체를 생성하고 Pizaa 함수(인스턴스?)에 "Two"를 대입한다.

        int n = Pizza.count; // static 변수의 count를 가져오기 때문에 n = 2 가 된다.
        System.out.println(n); // System.out.println();
    }
}
