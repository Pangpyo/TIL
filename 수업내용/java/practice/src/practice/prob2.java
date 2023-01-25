package practice;

import java.io.*;
import java.util.*;


public class prob2 {
	
	public static void main(String[] args) throws Exception{
		
		System.setIn(new FileInputStream("input2.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int tc = Integer.parseInt(br.readLine());
		int ans, x, y, d;
		int[] dx = {1, 0};
		int[] dy = {0, 1};
		for (int t = 1; t <= tc; t++) {
			String NK = br.readLine();
			st = new StringTokenizer(NK, " ");
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			int[][] pond = new int[N][N];
			int[][] bugs = new int[K][3];
			int[] jump = {0, 3, 2, 1};
			ans = 0;
			System.out.println(t + " " + N + " " + K);
			
			for (int k=0; k < K; k++) {
				String ijd = br.readLine();
				st = new StringTokenizer(ijd, " ");
				bugs[k][0] = Integer.parseInt(st.nextToken());
				bugs[k][1] = Integer.parseInt(st.nextToken());
				bugs[k][2] = Integer.parseInt(st.nextToken())-1;
			}
			external:
			for (int k=0; k < K; k++) {
				x = bugs[k][0];
				y = bugs[k][1];
				d = bugs[k][2];
				for (int j : jump){
					x += dx[d]*j;
					y += dy[d]*j;
					if (x >= N || x < 0 || y >= N || y < 0) {
						break;
					}
					if (pond[x][y] == 1) {
						ans = k+1;
						break external;
					}
					pond[x][y] = 1;
				}
			}
			sb.append("#"+ t + " " + ans + "\n");
		}
		System.out.println(sb);
	}
}
