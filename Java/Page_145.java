import javax.swing.*; // 윈도우 창을 생성하는 헤더파일 임포트

public class Page_145 {
    public static void main(String[] args){
        JFrame f = new JFrame("Frame Test"); // JFrame에서 f라는 객체를 만들고 타이틀을 "Frame Test" 라고 짓는다.

        f.setSize(100,100); // 윈도우창의 사이즈 설정 (가로, 세로)
        f.setVisible(true); // 볼 수 있도록 설정한다. true 본다, false 보지 않는다.
    }
}
