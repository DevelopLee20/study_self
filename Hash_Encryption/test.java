package hello;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

class Point{
      int x, y;
      public Point(int x, int y) {
         this.x = x;
         this.y = y;
      }
}

public class MyFrame extends JFrame {
   Image image;
   int x, y;
   ArrayList<Point> list = new ArrayList<Point>();
   
   class MyPanel extends JPanel implements Runnable{
         public void paint(Graphics g) {
            super.paint(g);
            for (Point p : list)
              g.drawImage(image,x,y,this);
         }
         public void run() {

            // 좌표 하나씩 받아서 그림 이동
            repaint();

            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
      }
   
   public MyFrame() {
      ImageIcon i = new ImageIcon("C:\\Users\\sseong\\문서\\cat.jpg");
       image = i.getImage().getScaledInstance(80, 80, Image.SCALE_SMOOTH);
      setSize(600, 400);
      setTitle("My Paint");
      MyPanel panel = new MyPanel();
      panel.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
               x = e.getX();
               y = e.getY();
               list.add(new Point(x, y));
            }
      });
      panel.addMouseListener(new MouseAdapter() {
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                System.out.println("mouseReleased");
                repaint(); 
                Thread t = new Thread(panel);
               t.start();    
            }
        });
       add(panel);
      setVisible(true);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
   public static void main(String[] args) {
      MyFrame f = new MyFrame();
   }
}
