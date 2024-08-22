package sudokuIrregular;
//import java.util.Random;

import java.awt.*;
import java.awt.Color;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JOptionPane;

@SuppressWarnings("serial")
public class Gui extends Frame {
	
	public Grid grid;
	public int currentlySelectedCol;
	public int currentlySelectedRow;
	public int markMode;
	public int numType;
	
	public Gui(){
		this.grid=new Grid(new Random().nextInt(2));
		currentlySelectedCol = 0;
		currentlySelectedRow = 0;
		numType=0;
		prepareGUI();
		
	}

	public void Run(Grid grid1){
		Gui window = new Gui();
		this.grid=grid1;
		print_help();
		window.setVisible(true);
	}
	
	public void Run(){
		Gui window = new Gui();
		print_help();
		window.setVisible(true);
	}
	
	public static void main(String[] args){
		Gui window = new Gui();
		window.print_help();
		window.setVisible(true);

	}
	

	
	private void prepareGUI(){
		setSize(600,650);
		// add the ability to close window
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent windowEvent){
			System.exit(0);
			}        
		});
		
		// mouse events
		addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
		        int x=e.getPoint().x, y=e.getPoint().y;
		        if(570>x && x>30 && 620>y && y>80) {
		        	x-=30;y-=80;
		        	if(y/60!=currentlySelectedRow && currentlySelectedCol!=x/60) {
		        		currentlySelectedRow = y/60;
			        	currentlySelectedCol = x/60;
		        	}
		        	else {
		        		currentlySelectedRow = 0;
			        	currentlySelectedCol = -1;
		        	}
		        }
		        repaint();
		    }
		});
		
		// mouse events
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
		        int key=e.getKeyChar(), keyCode = e.getKeyCode();;
		        
		        if('0'<key && key<='9') {
		        	if(markMode==0)
		        		grid.inputNumber(key-'0',currentlySelectedRow, currentlySelectedCol);
		        	else grid.inputMark(key-'0',currentlySelectedRow, currentlySelectedCol);
		        }
		        else if(key==KeyEvent.VK_BACK_SPACE || key==KeyEvent.VK_DELETE || key=='0')
		        	grid.inputNumber(0,currentlySelectedRow, currentlySelectedCol);
		        else if(key=='h')
		        	grid.getRandomGiven(grid, 0);
		        else if(key=='n')
		        	grid=new Grid(new Random().nextInt(2));
		        else if(key==KeyEvent.VK_ESCAPE){
		        	currentlySelectedCol = -1;
		    		currentlySelectedRow = -1;
		        }
		        else if(key=='r'){
		        	for(int i=0;i<9;i++) for(int j=0;j<9;j++) {
		        		if(grid.grid[i][j].given==0)
		        			grid.inputNumber(0,i, j);
		        	}
		        }
		        
		        switch(keyCode) { 
		        case KeyEvent.VK_UP:
		        	// handle up 
		        	if(currentlySelectedRow>0)
		        		currentlySelectedRow -=1;
		            break;
		        case KeyEvent.VK_DOWN:
		        	// handle down 
		        	if(currentlySelectedRow<8) 
		        		currentlySelectedRow +=1;
		            break;
		        case KeyEvent.VK_LEFT:
		            // handle left
		        	if(currentlySelectedCol>0) 
		        		currentlySelectedCol -=1;
		            break;
		        case KeyEvent.VK_RIGHT :
		            // handle right
		        	if(currentlySelectedCol<8) 
		        		currentlySelectedCol +=1;
		            break;
		        case KeyEvent.VK_SHIFT :
		            // handle shift
		        	markMode=markMode==1 ? 0:1;
		            break;
		        }
		        repaint();
		    }
		});
		
		String message = "you can solve with mouse and airrow keys \n\n"
		+"Shift key - turn markMode On/Off \n"
		+"Backspace/Del/0 key - delete number of not given cells \n"
		+"Esc key/Click same cell - stops focusing on cell \n\n"
		+"R key - resets all marking and inputed numbers \n"
		+"H key - get random hint \n"
		+"N key - get new puzzle \n";
		
		JOptionPane.showMessageDialog(new Frame(), message, "Key bindings",
		        JOptionPane.PLAIN_MESSAGE);
	}    
	
	public ArrayList<Integer> getCellMarks(int i, int j)
	{
		return this.grid.grid[i][j].marks;
	}
	
	public int getNumByType(int i, int j)
	{
		int num=-1;
		if(numType==0) return this.grid.getCellNum(i, j);
		if(numType==1) return this.grid.getCellSolvedNum(i, j);
		if(numType==2) return this.grid.getCellGroup(i, j);
		return num;
	}
	
	public void draw_cells(Graphics g2)
	{
		g2.setColor(new Color(0,0,0));
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				int num=getNumByType(i, j);
				if(num>0)
					g2.drawString(""+num, 50+j*60, 130+i*60);
				else if(!getCellMarks(i,j).isEmpty()) {
					ArrayList<Integer> marks=getCellMarks(i,j);
					g2.setFont(new Font("Serif", Font.PLAIN, 18));
					for(int z=0;z<marks.size();z++) {
						num=marks.get(z);
						g2.drawString(""+num, 38+j*60+((num-1)%3)*20, 98+i*60+((num-1)/3)*20);
					}
					g2.setFont(new Font("Serif", Font.PLAIN, 40));
				}
			}
		}
	}

	// grey=1, black=0  - grey = same group, black = different group
	public void drawXBorders(Graphics g2, int BlackOrGrey)
	{
		for(int i=0;i<9;i++) {
			for(int j=0;j<8;j++) {
				int bool=grid.getCellGroup(i, j)==grid.getCellGroup(i, j+1)? 1:0;
				if(bool==BlackOrGrey)
					if(i!=8)g2.fillRect(90+j*60, 80+i*60,4,64);
					else g2.fillRect(90+j*60, 80+i*60,4,60);
			}
		}
	}
	
	// grey=1, black=0  - grey = same group, black = different group
	public void drawYBorders(Graphics g2, int BlackOrGrey)
	{
		for(int i=0;i<8;i++) {
			for(int j=0;j<9;j++) {
				int bool=grid.getCellGroup(i, j)==grid.getCellGroup(i+1, j)? 1:0;
				if(bool==BlackOrGrey)
					if(j!=8)g2.fillRect(30+j*60, 140+i*60,64,4);
					else g2.fillRect(30+j*60, 140+i*60,60,4);
			}
		}
	}
	
	public void draw_borders(Graphics g2)
	{
		// draw grey borders
		g2.setColor(new Color(180,180,180));
		drawXBorders(g2,1);
		drawYBorders(g2,1);
		
		// draw black borders
		g2.setColor(new Color(0,0,0));
		drawXBorders(g2,0);
		drawYBorders(g2,0);
	}
	
	// grey=1, black=0  - grey = same group, black = different group
	public void draw_errors(Graphics g2)
	{
		g2.setColor(new Color(0,0,255));
		if(currentlySelectedRow>-1)
			g2.fillRect(30+currentlySelectedCol*60, 80+currentlySelectedRow*60,60,60);
		g2.setColor(new Color(250,0,0));
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				if(grid.getCellNum(i, j)!=grid.getCellSolvedNum(i, j) && grid.getCellNum(i, j)!=0)
					g2.fillRect(37+j*60, 87+i*60,50,50);
			}
		}
	}
	
	
	public void draw_text(Graphics g2)
	{
		// draw markMode
		g2.setFont(new Font("Serif", Font.PLAIN, 18));
		g2.drawString("markMode: "+markMode, 30, 70);
		// draw Sudoku Irregular
		g2.setFont(new Font("Serif", Font.PLAIN, 40));
		g2.drawString("Sudoku Irregular", 180, 60);
	}
	
	public void print_help()
	{
		System.out.println("	[Help]	");
		System.out.println("you can solve with mouse and keyboard \n");
		System.out.println("Shift key - turn markMode On/Off");
		System.out.println("Backspace/Del/0 key - delete number of not given cells");
		System.out.println("Esc key/Click same cell - stops focusing on cell \n");
		System.out.println("R key - resets all marking and inputed numbers");
		System.out.println("H key - get random hint");
		System.out.println("N key - get new puzzle");
	}
	
	
	@Override
	public void paint(Graphics g) {
		Graphics2D g2 = (Graphics2D)g;
		g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
				RenderingHints.VALUE_ANTIALIAS_ON);
		
		draw_text(g2);
		draw_errors(g2);
		g2.setColor(new Color(0,0,0));
		g2.drawRect(30, 80, 540, 540);
		draw_cells(g2);
		draw_borders(g2);
		
	}
}
