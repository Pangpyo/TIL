package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Bj16432 {
	
	
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		String[][] D = new String[N][10];
		int m;
		int[][] cakes = new int[N][];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken());
			int[] cake = new int[m];
			for (int j=0; j<m; j++) {
				cake[j] = Integer.parseInt(st.nextToken());
			}
			cakes[i] = cake;
		}
		for (int i : cakes[0]) {
			D[0][i] = Integer.toString(i);
		}
		for (int i=1; i<N; i++) {
			for (int cake : cakes[i]) {
				for (int j=1; j<10; j++) {
					if (j == cake || D[i-1][j] == null) {
						continue;
					}
					D[i][cake] = D[i-1][j] + cake;
					break;
				}
			}
		}

		for (String d : D[N-1]) {
			if (d != null) {
				for (int i=0; i < d.length(); i++) {
					System.out.println(d.charAt(i));
				}
				return;
			}
		}
		System.out.println(-1);
	}
}
