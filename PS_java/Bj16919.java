
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int[][] map;
	static int R, C, N;

	static void putBomb() {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (map[i][j] == 0)
					map[i][j] = 4;
			}
		}
	}

	static void time(boolean flag) {
		ArrayList<int[]> list = new ArrayList<>();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (map[i][j] > 0) {
					map[i][j]--;
					if (flag && map[i][j] == 0)
						list.add(new int[] { i, j });
				}
			}
		}
		for (int[] xy : list) {
			explode(xy[0], xy[1]);
		}
	}

	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	static void explode(int x, int y) {
		int nx, ny;
		for (int i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx >= R || nx < 0 || ny >= C || ny < 0)
				continue;
			map[nx][ny] = 0;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		String temp;
		map = new int[R][C];
		for (int i = 0; i < R; i++) {
			temp = br.readLine();
			for (int j = 0; j < C; j++) {
				if (temp.charAt(j) == 'O')
					map[i][j] = 3;
			}
		}
		
		
		int nN=0;
		if (N == 1) nN = 0;
		else if(N % 2 == 0) nN = 2;
		else if(N % 4 == 3) nN = 3;
		else if(N % 4 == 1) nN = 4;
		for (int i = 0; i < nN; i++) {
			putBomb();
			time(true);
//			System.out.println(i);
//			for (int j = 0; j < R; j++) {
//				System.out.println(Arrays.toString(map[j]));
//			}
			
		}
		StringBuilder sb = new StringBuilder();
		
		
		
		
		
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				sb.append(map[i][j] > 0 ? 'O' : '.');
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}