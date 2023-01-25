package practice;

import java.util.*;
import java.io.*;

public class prob3 {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("input3.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int tc, N, x, y, J, M, d, n, jx, jy;
		String NxyM;
		String sjumper;
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, 1, 0, -1};
		tc = Integer.parseInt(br.readLine());

		for (int t = 1; t <= tc;t++) {
			NxyM = br.readLine();
			st = new StringTokenizer(NxyM, " ");
			N = Integer.parseInt(st.nextToken());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			J = Integer.parseInt(st.nextToken());
			sjumper = br.readLine();
			st = new StringTokenizer(sjumper, " ");
			int[][] map = new int[N][N];
			for (int j=0; j<J; j++) {
				jx = Integer.parseInt(st.nextToken());
				jy = Integer.parseInt(st.nextToken());
				map[jx-1][jy-1] = 1;
			}
			M = Integer.parseInt(br.readLine());
//			int[][] move = new int[M][2];
			st = new StringTokenizer(br.readLine(), " ");
			external:
			for (int m=0; m<M; m++) {
				d = Integer.parseInt(st.nextToken())-1;
				n = Integer.parseInt(st.nextToken());
				for (int i=1; i<=n;i++) {
					x += dx[d];
					y += dy[d];
					if (x >= N || x < 0 || y >= N || y < 0) {
						x = 0;
						y = 0;
						break external;
					}
					if (map[x][y] == 1) {
						x = 0;
						y = 0;
						break external;
					}
				}
			}

			
			System.out.printf("#%d %d %d\n", t, x, y);
		}
	}
}
