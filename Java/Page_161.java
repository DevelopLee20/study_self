class Pizza{ // Pizza 클래스
    int radius; // 변수 선언

    Pizza(int r){ // 기본 생성자
        radius = r;
    }

    Pizza whosLargest(Pizza p1, Pizza p2){ // Pizza의 객체를 받아서? 변수 생성, Pizza 메소드 사용
        if (p1.radius > p2.radius){ // 객체 2개를 비교
            return p1;
        }
        else{
            return p2;
        }
    }
}

public class Page_161 {
    public static void main(String[] args){
        Pizza obj1 = new Pizza(14); // 객체 생성
        Pizza obj2 = new Pizza(18); // 객체 생성
        // obj1. 이 부분은 객체를 위한 부분이기 때문에 객체를 생성한 아무 변수에서 사용 가능하다.
        Pizza largest = obj1.whosLargest(obj1, obj2); // 생성된 객체 2개를 whosLargest에서 사용
        System.out.println(largest.radius); // Pizza largest객체의 radius 값을 출력
        // largest를 출력하고자 하면 주소값이 나옴
    }
}
