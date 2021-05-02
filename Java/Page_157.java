import java.math.*;

class MyMath{
    public static int abs(int x){ // 정적 public, class 내부에 함수?가 여러 개 이므로 static, int형 abs 이름
        return x>0?x:-x; // 만약 x가 0보다 크면, x를 리턴, 아니면 -x를 리턴
    }

    public static int power(int base, int exponent){ // 정적 public, class 내부 함수?가 여러 개 이므로 static, int 형 power 이름
        int result = 1; // result 라는 변수 선언
        for (int i = 1; i <= exponent; i++){ // 반복
            result += base; // 증감 연산자
        }
        return result; // 결과값을 반환한다.
    }
}

public class Page_157 {
    public static void main(String[] args){
        System.out.println(MyMath.power(10,3)); // System.out.println(); MyMath.power(매개변수1,매개변수2);
    }
}
