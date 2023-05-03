import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static boolean check(int n, int ud) {
		if (n - ud >= 0 && n - ud < 10)
			return true;
		return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[][][] D = new int[N][10][1<<10];
		
		for (int i=1; i<10; i++) {
			D[0][i][1<<i] = 1;
		}
		int M = 1000000000;
		for (int n=0; n<N-1; n++) {
			for (int i=0; i<10; i++) {
				for (int j=0; j<(1<<10); j++) {
					if (D[n][i][j] == 0) continue;
					if (i > 0) {
						D[n+1][i-1][j|(1<<(i-1))] += D[n][i][j];
						D[n+1][i-1][j|(1<<(i-1))] %= M; 
					}
					if (i < 9) {
						D[n+1][i+1][j|(1<<(i+1))] += D[n][i][j];
						D[n+1][i+1][j|(1<<(i+1))] %= M; 
					}
				}
			}
		}

	
		
		int ans = 0;
		for (int i=0; i<10; i++) {
			ans += D[N-1][i][(1<<10)-1];
			ans %= M;
		}
		System.out.println(ans);

	}
}