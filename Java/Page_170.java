class Circle{ // class 이름이 Circle
    class Point{ // Class 내부의 class Point
        int x, y; // 변수선언
        
        public Point(int x, int y){ // 메소드 생성
            this.x = x; // this.x != x
            this.y = y; // this.y != y
        }
    }

    int radius; // int형 변수 선언
    Point center; // class Point의 center 변수

    public Circle(int radius, int x, int y){ // 3개의 매개변수를 가진 public 메소드
        this.radius = radius; // this.radius != radius
        this.center = new Point(x,y); // this.center는 Point class에서 가져오고, Point라는 객체를 생성해서 this.x , this.y를 정한다.
    }

    double calcArea(){ // calcArea 메소드
        return 3.14 * radius * radius; // return 함
    }
}

public class Page_170 {
    Circle obj = new Circle(10,0,0); // Circle 객체를 생성한다. 매개변수는 10,0,0
    System.out.println(obj.calcArea()); // obj.calcArea() 생성
}
