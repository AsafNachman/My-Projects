package sudokuIrregular;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Grid {
	Cell grid[][];
	int firstFromGroup[];
	int difficulty;
	
	public Grid(int difficulty) {
		this.grid=new Cell[9][9];
		this.firstFromGroup = new int[9];
		for(int i=0;i<9;i++) {
			firstFromGroup[i]=-1;
			for(int j=0;j<9;j++)
				this.grid[i][j]=new Cell();
		}
		this.difficulty=difficulty;
		// 0 is easiest difficuly, bellow it is a clean grid
		if(difficulty>-1)
			getRandomPuzzle();
	}
	
	public Grid() {
		this(new Random().nextInt(3));
	}
	
	public void getRandomPuzzle()
	{
		// loops until it generates solvable solved puzzle
		while(generateRandomSolvedPuzzle()==-1); 
		getGivenNumbers();
	}
	
	public int generateRandomSolvedPuzzle()
	{
		getRandomGroups(); // its more efficient to getRandomGroups here
		return generateRandomSolvedNumbers();
	}
	
	
	public int generateRandomSolvedNumbers()
	{
		Random rand = new Random();
		int counter2=0,counter=0,num,x=rand.nextInt(9),y=rand.nextInt(9);
		// resets this.grid
		for (int i=0;i<9;i++){for(int j=0;j<9;j++) { this.grid[i][j].resetNumber();}}
		// loops until all 81(9*9) numbers are inputed
		while(counter!=81) {
			// some random configurations arent solvable so if it loops more than 500000 times it resets
			if(counter2>500000) return -1;
			num=getCellSolvedNum(x, y);
			if(num<1) num=1; // if num bellow 1 make it one
			// +1 to num until its a safe input, if its gets to 10 it will be "safe"
			while(isSafe(num,x,y)==-1) num++;
			// if its 10, than we need to go backwards make it possible
			if(num>9) {
				this.grid[x][y].solvedNum=-1; // resets current number
				x--;
				if(x==-1) {
					x=8;
					y--;
					if(y<0) y=8;
				}
				this.grid[x][y].solvedNum++; // adds one to its previous number
				counter--;
			}
			// if its bellow 10(it a given its above 0) than input it into the grid
			else {
				this.grid[x][y].solvedNum=num;
				x++;
				if(x>8) {
					x=0;
					y++;
					if(y>8) y=0;
				}
				counter++;
			}
			counter2++; // counts the number of loops
		}
		return 1;
	}
	
	// checks if a number in possition i,j is safe based on solved numbers
	public int isSafe(int num ,int x ,int y)
	{
		int i,j, counter=0, groupNum=this.grid[x][y].group;
		
		for(i=0;i<9;i++) {
			// check column x
			if(this.grid[i][y].solvedNum==num) return -1;
			
			// check row y
			if(this.grid[x][i].solvedNum==num) return -1;
		}
		
		// check group
		for(i=this.firstFromGroup[groupNum];i<9 && counter<9;i++) {
			for(j=0;j<9;j++) {
				if(this.grid[i][j].group==groupNum) {
					if(this.grid[i][j].solvedNum==num) return -1;
					counter++;
				}
			}
		}
		return 1;
	}
	
	
	public void getGivenNumbers()
	{
		int i,j,generate=40-5*difficulty;
		Grid newGird = new Grid(-1);
		// copies this.firstFromGroup and this.grid into the newGrid
		for(i=0;i<9;i++) {
			newGird.firstFromGroup[i]=this.firstFromGroup[i];
			for(j=0;j<9;j++)
				newGird.grid[i][j].group=this.grid[i][j].group;
		}
		while(generate--!=0) {
			getRandomGiven(newGird);
		}
		makeSolvable(newGird, 0);
	}
	
	public void getRandomGiven1(Grid newGird, int given)
	{
		Random rand = new Random();
		int x=rand.nextInt(9),y=rand.nextInt(9), counter2=0;
		while(newGird.grid[x][y].num!=0 && counter2++!=1000) {
			x=rand.nextInt(9);
			y=rand.nextInt(9);
		}
		
		newGird.grid[x][y].setNum(this.grid[x][y].solvedNum);
		if(given==0) newGird.grid[x][y].given=0;
	}
	
	public void getRandomGiven(Grid newGird, int given)
	{
		getRandomGiven1(newGird, given);
	}
	
	public void getRandomGiven(Grid newGird)
	{
		getRandomGiven1(newGird, 1);
	}
	
	

	
	// adds a given number until solvable
	// if 10 numbers above difficulty given numbers resets newGrid and starts all over again
	public void makeSolvable(Grid newGird, int counter)
	{
		// until solvable add a new random given number (to make more solvable)
		while(newGird.isSolvable1()==-1) {
			getRandomGiven(newGird);
			counter++;
		}
		// each difficulty can only be 40-5*difficulty with max 10 above
		if(counter>10) {
			getGivenNumbers();
			return;
		}
		this.grid=newGird.grid.clone();
	}
	
	
	// version1 to check if solvable
	public int isSolvable()
	{
		int i,j;
		this.Solve();
		for(i=0;i<9;i++)
			for(j=0;j<9;j++)
				if(isSafe(getCellSolvedNum(i, j), i, j)==-1) return -1;
		return 1;
	}

	
	// version2 to check if solvable - this is used because it faster
	public int isSolvable1()
	{
		Solve();
		int i,j,k;
		// check rows
		ArrayList<Integer> possibilitiesX = new ArrayList<Integer>();
		ArrayList<Integer> possibilitiesY = new ArrayList<Integer>();
		
		for(i=0;i<9;i++) {
			// reset possibilities
			for(j=1;j<10;j++) {possibilitiesX.add(j); possibilitiesY.add(j);}
			for(j=0;j<9;j++) {
				// checks if rows have all the 1 to 9 numbers
				if(possibilitiesX.contains(getCellSolvedNum(i, j)))
					possibilitiesX.remove(Integer.valueOf(getCellSolvedNum(i, j)));
				else return -1;
				// checks if columns have all the 1 to 9 numbers
				if(possibilitiesY.contains(getCellSolvedNum(j, i)))
					possibilitiesY.remove(Integer.valueOf(getCellSolvedNum(j, i)));
				else return -1;
			}
			possibilitiesX.clear();possibilitiesY.clear();
		} 
		
		// check groups
		for(k=0;k<9;k++) {
			// reset possibilities
			for(j=1;j<10;j++) {possibilitiesX.add(j);}
			for(i=0;i<9;i++) {
				for(j=0;j<9;j++) {
					if(getCellGroup(i, j)==k)
						// checks for every group if it has all the 1 to 9 numbers
						if(possibilitiesX.contains(getCellSolvedNum(i, j)))
							possibilitiesX.remove(Integer.valueOf(getCellSolvedNum(i, j)));
						else return -1;
				}
			}
			possibilitiesX.clear();
		}
		return 1;
	}
	
	// generates random grid groups until one is solvable is made
	public void getRandomGroups() { while(generateRandomGroups()==-1); getFirstsFromGroups();}
	
	public int generateRandomGroups()
	{
		int i,j,z,randomNum,groupNum;
		// random groups
		for(i=0;i<9;i++) for(j=0;j<9;j++) {this.grid[i][j].group=-1;}
		for(groupNum=0;groupNum<9;groupNum++) {
			// finds the first i,j that is available
			i=0;
			j=0;
			while(this.grid[i][j].group!=-1) {
				j++;
				if(j==9) {
					j=0;
					i++;
				}
			}
			// makes the first i,j available start a new group
			this.grid[i][j].group=groupNum;
			
			// makes the other 8 cells in the group randomly
			for(z=0;z<8;z++) {
				randomNum=getRandomPossibility(i, j);
				if(randomNum==-1) return -1;
				if(randomNum==0){
					i-=1;
					this.grid[i][j].group=groupNum;
				}
				else if(randomNum==1 && j>0) {
					j-=1;
					this.grid[i][j].group=groupNum;
				}
				else if(randomNum==2 && i<8) {
					i+=1;
					this.grid[i][j].group=groupNum;
				}
				else if(randomNum==3 && j<8) {
					j+=1;
					this.grid[i][j].group=groupNum;
				}
			}
		}
		return 1;
	}
	
	public int getRandomPossibility(int i, int j)
	{
		ArrayList<Integer> possibilities = new ArrayList<Integer>();
		Random rand = new Random();
		// checks which turn for i,j are possible and adds them to possibilities
		if(i>0) if(this.grid[i-1][j].group==-1)
			possibilities.add(0);
		if(j>0) if(this.grid[i][j-1].group==-1)
			possibilities.add(1);
		if(i<8) if(this.grid[i+1][j].group==-1)
			possibilities.add(2);
		if(j<8) if(this.grid[i][j+1].group==-1)
			possibilities.add(3);
		// if none are available return
		if(possibilities.size()==0) return -1;
		// return a random possibility from them
		return possibilities.get(rand.nextInt(possibilities.size()));
	}
	
	
	
	// sets firstFromGroup - marks the first cells from groups for better efficiency
	public void getFirstsFromGroups() {
		// resets firstFromGroup and finds the first from groups
		for(int i=0;i<9;i++) {firstFromGroup[i]=-1;}
		for(int i=0;i<9;i++)
			for(int j=0;j<9;j++) {
				int num=getCellGroup(i, j);
				if(firstFromGroup[num]==-1)
					firstFromGroup[num]=i;
			}
	}
	
	
	
	// remove all false possibilities from cells
	public void Solve() 
	{
		getFirstsFromGroups();
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				int num=getCellSolvedNum(i, j);
				if(num!=0) {
					RemoveGroupPossibilities(this.grid[i][j].group,num);
					RemoveColRowPossibilities(num,i, j);
				}
			}
		}
	}
	
	
	// remove possibilities of a number from all of its group cells
	public void RemoveGroupPossibilities(int groupNum, int num) {
		int i,j,counter=0;
		for(i=this.firstFromGroup[groupNum];i<9 && counter<9;i++) {
			for(j=0;j<9;j++) {
				if(this.grid[i][j].group==groupNum) {
					if(this.grid[i][j].possibilities.contains(Integer.valueOf(num)))
						this.grid[i][j].possibilities.remove(Integer.valueOf(num));
					counter++;
					lastPossibility(i,j);
				}
			}
		}
	}
	
	
	// remove possibilities of a number from row i and column j
	public void RemoveColRowPossibilities(int num,int i, int j)
	{
		for(int k=0;k<9;k++) {
			// remove all num from column i
			lastPossibility(k, j);
			if(this.grid[k][j].possibilities.contains(Integer.valueOf(num)))
				this.grid[k][j].possibilities.remove(Integer.valueOf(num));
			
			
			// remove all num from row j
			lastPossibility(i, k);
			if(this.grid[i][k].possibilities.contains(Integer.valueOf(num)))
				this.grid[i][k].possibilities.remove(Integer.valueOf(num));
		}
	}
	
	// checks if last possibility, if it is make its solvedNum equal to its last possibility 
	public void lastPossibility(int i, int j)
	{
		if(this.grid[i][j].possibilities.size()==1) { 
			this.grid[i][j].solvedNum=this.grid[i][j].possibilities.get(0);
			RemoveGroupPossibilities(this.grid[i][j].group,this.grid[i][j].solvedNum);
			RemoveColRowPossibilities(this.grid[i][j].solvedNum, i, j);
			this.grid[i][j].possibilities.clear();
		}
	}
	
	
	// print solvedGridNumbers
	public void printSolvedGrid()
	{
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				System.out.print(this.grid[i][j].solvedNum + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	
	// print solvedGridNumbers
	public void printGroupGrid()
	{
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				System.out.print(this.grid[i][j].group + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	
	public void inputNumber(int num,int x, int y)
	{
		if(this.grid[x][y].given==0) {
			this.grid[x][y].num=num;
			this.grid[x][y].marks.clear();
		}
	}
	
	public void inputMark(int num,int x, int y)
	{
		if(this.grid[x][y].given==0) {
			if(this.grid[x][y].marks.contains(Integer.valueOf(num)))
				this.grid[x][y].marks.remove(Integer.valueOf(num));
			else
				this.grid[x][y].marks.add(Integer.valueOf(num));
			Collections.sort(this.grid[x][y].marks);
		}
	}
	
	public int getCellNum(int i, int j) {
		return this.grid[i][j].num;
	}
	
	public void setCellNum(int i, int j, int num) {
		this.grid[i][j].setNum(num);;
	}
	
	public int getCellGroup(int i, int j) {
		return this.grid[i][j].group;
	}
	
	public int getCellSolvedNum(int i, int j) {
		return this.grid[i][j].solvedNum;
	}
	
	
	
	
	
	// hand made solvable sudoku puzzle
	public void test1()
	{
		this.grid[0][0] = new Cell(7,1);
		this.grid[0][1] = new Cell(3,1);
		this.grid[0][2] = new Cell(0,1);
		this.grid[0][3] = new Cell(1,1);
		this.grid[0][4] = new Cell(8,1);
		this.grid[0][5] = new Cell(6,2);
		this.grid[0][6] = new Cell(0,2);
		this.grid[0][7] = new Cell(2,2);
		this.grid[0][8] = new Cell(4,2);
		
		this.grid[1][0] = new Cell(9,1);
		this.grid[1][1] = new Cell(4,1);
		this.grid[1][2] = new Cell(0,3);
		this.grid[1][3] = new Cell(0,3);
		this.grid[1][4] = new Cell(0,4);
		this.grid[1][5] = new Cell(0,5);
		this.grid[1][6] = new Cell(0,5);
		this.grid[1][7] = new Cell(3,2);
		this.grid[1][8] = new Cell(1,2);
		
		this.grid[2][0] = new Cell(0,1);
		this.grid[2][1] = new Cell(7,3);
		this.grid[2][2] = new Cell(0,3);
		this.grid[2][3] = new Cell(8,4);
		this.grid[2][4] = new Cell(0,4);
		this.grid[2][5] = new Cell(1,4);
		this.grid[2][6] = new Cell(0,5);
		this.grid[2][7] = new Cell(9,5);
		this.grid[2][8] = new Cell(0,2);
		
		this.grid[3][0] = new Cell(0,1);
		this.grid[3][1] = new Cell(0,3);
		this.grid[3][2] = new Cell(0,4);
		this.grid[3][3] = new Cell(7,4);
		this.grid[3][4] = new Cell(2,4);
		this.grid[3][5] = new Cell(3,4);
		this.grid[3][6] = new Cell(0,4);
		this.grid[3][7] = new Cell(0,5);
		this.grid[3][8] = new Cell(0,2);
		
		this.grid[4][0] = new Cell(4,6);
		this.grid[4][1] = new Cell(0,3);
		this.grid[4][2] = new Cell(0,7);
		this.grid[4][3] = new Cell(0,7);
		this.grid[4][4] = new Cell(3,7);
		this.grid[4][5] = new Cell(0,7);
		this.grid[4][6] = new Cell(0,7);
		this.grid[4][7] = new Cell(0,5);
		this.grid[4][8] = new Cell(7,2);
		
		this.grid[5][0] = new Cell(8,6);
		this.grid[5][1] = new Cell(0,3);
		this.grid[5][2] = new Cell(0,3);
		this.grid[5][3] = new Cell(4,7);
		this.grid[5][4] = new Cell(0,7);
		this.grid[5][5] = new Cell(5,7);
		this.grid[5][6] = new Cell(0,5);
		this.grid[5][7] = new Cell(0,5);
		this.grid[5][8] = new Cell(9,8);
		
		this.grid[6][0] = new Cell(0,6);
		this.grid[6][1] = new Cell(0,3);
		this.grid[6][2] = new Cell(1,0);
		this.grid[6][3] = new Cell(0,0);
		this.grid[6][4] = new Cell(9,7);
		this.grid[6][5] = new Cell(0,0);
		this.grid[6][6] = new Cell(6,0);
		this.grid[6][7] = new Cell(4,5);
		this.grid[6][8] = new Cell(0,8);

		this.grid[7][0] = new Cell(1,6);
		this.grid[7][1] = new Cell(0,6);
		this.grid[7][2] = new Cell(2,0);
		this.grid[7][3] = new Cell(0,0);
		this.grid[7][4] = new Cell(0,0);
		this.grid[7][5] = new Cell(0,0);
		this.grid[7][6] = new Cell(8,0);
		this.grid[7][7] = new Cell(0,8);
		this.grid[7][8] = new Cell(3,8);
		
		this.grid[8][0] = new Cell(3,6);
		this.grid[8][1] = new Cell(2,6);
		this.grid[8][2] = new Cell(0,6);
		this.grid[8][3] = new Cell(9,6);
		this.grid[8][4] = new Cell(1,8);
		this.grid[8][5] = new Cell(4,8);
		this.grid[8][6] = new Cell(0,8);
		this.grid[8][7] = new Cell(8,8);
		this.grid[8][8] = new Cell(6,8);
	}
}
