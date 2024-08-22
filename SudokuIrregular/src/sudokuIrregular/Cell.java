package sudokuIrregular;
import java.util.ArrayList;
import java.util.Random;

public class Cell {
	int num;
	ArrayList<Integer> possibilities;
	ArrayList<Integer> marks;
	int solvedNum;
	int group;
	int given;
	
	public Cell(int num, int group) {
		this.num=num;
		this.given=0;
		this.solvedNum=-1;
		this.group=group;
		this.marks = new ArrayList<Integer>();
		this.possibilities = new ArrayList<Integer>();
		if(num==0)
			for(int i=1;i<10;i++) {this.possibilities.add(i);}
		else
			this.solvedNum=num;
	}
	
	public Cell(int group) {
		this(0,group);
	}
	
	public Cell() {
		this(0,-1);
	}

	public int getNum() {
		return num;
	}

	public void resetNumber() {
		this.num=0;
		this.given=0;
		this.solvedNum=-1;
		this.possibilities.clear();
		this.marks.clear();
		for(int i=1;i<10;i++) {this.possibilities.add(i);}
	}
	
	public void setNum(int num) {
		this.num = num;
		this.given=1;
		this.solvedNum=num;
		this.possibilities.clear();
		this.marks.clear();
	}

	public int getSolvedNum() {
		return solvedNum;
	}

	public void setSolvedNum(int solvedNum) {
		this.solvedNum = solvedNum;
		this.possibilities.clear();
	}
	
	public int getRandomPossibility() {
		return possibilities.get(new Random().nextInt(possibilities.size()));
	}
	
	public void setARandomPossibility() {
		setNum(getRandomPossibility());
		
	}
	
}
