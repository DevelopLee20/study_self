public class Page_45 {
    public static void main(String[] args){
        // final은 상수를 선언할 때 사용한다.
        final double light_speed = 30e4; // light_speed는 이제 실수를 의미한다. 부동소수점을 표시한다. 30 x 10^4 와 같은 의미이다.
        double distance = 30e12; // 30 xx 10^12와 같은 의미이다.
        double secs; // double형은 실수형이다.
        secs = distance/light_speed;
        double light_year = secs/(60.0*60.0*24.0*365.0);
        System.out.println("time: "+light_year);
    }
}
