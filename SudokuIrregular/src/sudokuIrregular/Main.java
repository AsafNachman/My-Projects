package sudokuIrregular;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Grid grid1 = new Grid();
		test_gui(grid1);
		
	}
	
	public static void test_gui(Grid grid1)
	{
		Gui screen = new Gui();
		screen.Run(grid1);
	}
	
}
