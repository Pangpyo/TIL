package practice;

import java.util.*;
import java.io.*;

public class prob1 {
	public static void main(String[] args) throws Exception {
		

		System.setIn(new FileInputStream("input1.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(br.readLine());
		for (int t = 1; t <= tc; t++) {
			int n = Integer.parseInt(br.readLine());
			
			char[][] a = new char[n][n];
			
			for (int i = 0; i< n; i++) {
				String[] split = br.readLine().split(" ");
				for (int j = 0; j < n; j++) {
					a[i][j] = split[j].charAt(0);
				}
			}
			
			int[] dx = {0, 0, 1, -1};
			int[] dy = {1, -1, 0, 0}; 
			int cnt = 0;
			for (int x = 0; x < n; x++) {
				for (int y = 0; y < n; y++) {
					int d = 0;
					if (a[x][y] == 'A') {
						d = 1;
					}
					else if (a[x][y] == 'B'){
						d = 2;
					}
					else if (a[x][y] == 'C') {
						d = 4;
					}
					for (int i = 0; i < d; i++) {
						int j = 1;
						while (true) {
							int nx = x + dx[i]*j;
							int ny = y + dy[i]*j;
							j++;
							if (0 <= nx & nx < n & 0 <= ny & ny < n ) {
								if (a[nx][ny] == 'S') {
									cnt++;
								}
								else {
									break;
								}
							}
							else {
								break;
							}
						}
						
					}
				}
			}
			
			System.out.printf("#%d %d\n", t, cnt);
			
			
		}
	}
}
