import java.awt.*;
import javax.swing.*;

public class RadioButtonJFrame extends JFrame implements ActionListener{

    private JRadioButton small, medium, largs;
    private JLabel text;
    private JPanel topPanel, sizePanel, resultJPanel;

    public RadioButtonJFrame(){
        setTitle("setTitle");
        setSize(300,150);
    }
}