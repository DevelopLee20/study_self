public class Page_89 {
    public static void main(String args[]){
        for (int i = 0; i < 5; i++){ // for 문에 의한 반복
            if (i%3 == 0){
                continue; // 조건이 성립하면 continue 문이 실행되는데, 이때 아래 부분이 실행되지 않고 그냥 넘어간다.
            }
            System.out.println(i);
        }
    }
}
