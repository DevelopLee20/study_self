public class Page_56 {
    public static void main(String args[]){
        int x = 1;
        int y = 1;

        int nextx = ++x; // 증감 연산자 더 한 후 대입
        int nexty = y++; // 증감 연산자 대입한 후 더함
        System.out.println(nextx+nexty);
    }
}
