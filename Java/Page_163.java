public class Page_163 { // 파일명 public class 파일명

    public static double minArray(double[] list){ // 클래스 외부에서도 사용가능하지만 하나밖에 없는 double 형 minArray인데 매개변수가 double형 리스트이다.
        double min = list[0]; // double 형 변수 선언

        for (int i = 1; i < list.length; i++){ // list.length = 매개변수로 받은 리스트의 크기 만큼 반복
            if (list[i] < min){ // 최소값을 찾는 알고리즘
                min = list[i];
            }
        }
            return (min);
    }

    public static void main(String[] args){
        double[] a = {1.1,2.2,3.3,4.4,5.5}; // 리스트 a 선언
        double[] b = {-2.0,3.0,-4.9}; // 리스트 b 선언

        double min; // double 형 min 변수

        min = minArray(a); // min 변수는 minArray에 a를 넣는다. 이때 클래스 내부에 있기 때문에 객체 생성은 하지 않는다.
        System.out.println(a); // System.out.println();
        min = minArray(b); // minArray에 b를 넣는다. 이때 클래스 내부에 있어 객체는 생성하지 않는다.
        System.out.println(b); // System.out.println();
    }
}
