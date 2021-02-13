public class Page_134 {
    private int channel;
    private int volume;
    
    Television(int c, int v) {
        channel = c;
        volume = v;
    }

    void print(){
        System.out.println(channel+volume);
    }

    public static void main(String[] args){
        Television myTv = new Television(7,10);
        myTv.print();
        Television yourTv = new Television(11,20);
        yourTv.print();
    }
}
