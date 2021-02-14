public class Page_134 {

    private int channel; // private 클래스 내에서만 접근 가능
    private int volume; // private 클래스 내에서만 접근 가능
    
    Page_134(int c, int v) { // 생성자 정의, 클래스의 내용이 모두 이 생성자를 따른다.
        channel = c;
        volume = v;
    }

    void print(){
        System.out.println(channel+volume);
    }

    public static void main(String[] args){
        Page_134 myTv = new Page_134(7,10); // 객체 생성
        myTv.print(); // 함수 호출
        Page_134 yourTv = new Page_134(11,20); // 객체 생성
        yourTv.print(); // 객체를 이용한 함수 호출
    }
}
