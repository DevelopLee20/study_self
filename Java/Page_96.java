import java.util.Arrays; // Arrays 헤더? 파일을 import함

public class Page_96 {
    public static void main(String[] args){
        int[] numbers = {10,20,30}; // int형 배열 선언 및 초기화
        int[][] two_numbers = new int[3][3]; // 2차원 배열 선언 및 new에 의한 초기화
        two_numbers[1][1] = 3; // 2차원 배열 초기화
        int[][] reset_num = {{1,2,3},{3,4,5}}; // 하드코딩을 사용한 배열 초기화
        System.out.println(reset_num);
        for (int value : numbers){ // value 값이 numbers의 배열 요소 하나하나씩에 저장된다.
            System.out.println(value); // value를 출력함
            System.out.println(Arrays.toString(numbers)); // 배열의 모든 요소를 출력함. java.util 필요
            // Arrays.toString(배열이름);
        }
    }
}
