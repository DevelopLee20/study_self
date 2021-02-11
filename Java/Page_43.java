public class Page_43 {
    public static void main(String[] args){
        long lightspeed; // long형은 int 자료형과 같은 범위를 가지는 정수형이다.
        long distance; // long형은 int 자료형과 같은 범위를 가지는 정수형이다.
        // 전공책에서는 long 형이 int형 보다 더 넓은 범위를 커버할 수 있다고 한다.

        lightspeed = 300000; // 변수 초기화
        distance = lightspeed * 365L * 24 * 60 * 60; // L은 식별자를 의미하며, long 형이라는 뜻이다.
    
        System.out.println("distance: "+distance); // System.out.println();
    }
}
