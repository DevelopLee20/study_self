public class Page_79 {
    public static void main(String args[]){
        int i = 1;
        int sum = 0;
        while (i <= 10){ // 반복문 while을 사용해서 무한으로 돌림, 조건이 있을때 true 일 경우 돌리고 False 일 경우 멈춘다.
            sum = sum + i;
            i++;
        }
        System.out.println(sum+i);
    }
}
