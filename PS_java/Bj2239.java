import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int[] row = new int[9];
	static int[] col = new int[9];
	static int[] sqr = new int[9];
	static int[][] board = new int[9][9];
	static List<Integer> empty = new ArrayList<Integer>();
	static boolean flag = false;
	
	
	
	static void sdoku(int n, int cnt) {
		if (flag) return;
		if (cnt == empty.size()) {
			for (int i=0; i<9; i++) {
				for (int j=0; j<9; j++) {
					System.out.print(board[i][j]);
				}
				System.out.println();
			}
			flag = true;
			return;
		}
		int x = empty.get(n)/9;
		int y = empty.get(n)%9;
		for (int i=1; i<=9; i++) {
			if ((row[x] & 1<<i) != 0) continue;
			if ((col[y] & 1<<i) != 0) continue;
			if ((sqr[(x/3)*3+(y/3)] & 1<<i) != 0) continue;
			row[x] |= 1<<i;
			col[y] |= 1<<i;
			sqr[(x/3)*3+(y/3)] |= 1<<i;
			board[x][y] = i;
			
			sdoku(n+1, cnt+1);
			row[x] -= 1<<i;
			col[y] -= 1<<i;
			sqr[(x/3)*3+(y/3)] -= 1<<i;
			board[x][y] = 0;
		}
	}
	
	

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String str;
		int temp;
		
		for (int i=0; i<9; i++) {
			 str = sc.next();
			 for (int j=0; j<9; j++) {
				 temp = str.charAt(j)-'0';
				 board[i][j] = temp;
				 row[i] |= 1<<temp;
				 col[j] |= 1<<temp;
				 sqr[(i/3)*3+(j/3)] |= 1<<temp;
				 if (temp == 0) empty.add(i*9+j); 
			 }
		}
		sdoku(0, 0);
	}
	
}