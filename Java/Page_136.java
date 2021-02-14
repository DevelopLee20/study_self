public class Page_136 {
    int radius; // 변수

    public Page_136(int radius){
        this.radius = radius; // this.radius 는 필드이고, radius는 매개 변수이다.
    }

    double calcArea(){
        return 3.14*radius+radius; // 3.14*메개변수*매개변수
    }
}
