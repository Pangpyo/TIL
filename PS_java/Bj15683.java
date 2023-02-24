import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;



public class Main {
	static int N, M, ans;
	static int[][] map;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static List<int[]> cctv;
	
	static void see(int n, int d, int x, int y) {
		int[] see = null;
		switch (n) {
		case 1:
			see = new int[] {0};
			break;
		case 2:
			see = new int[] {0, 2};
			break;
		case 3:
			see = new int[] {0, 3};
			break;
		case 4:
			see = new int[] {0, 2, 3};
			break;
		case 5:
			see = new int[] {0, 1, 2, 3};
			break;
		}
		int nx, ny, nd;
		for (int i=0; i<see.length; i++) {
			nd = (see[i]+d)%4;
			nx = x;
			ny = y;
			while (true) {
				if (0<=nx && nx<N && 0<=ny && ny<M && map[nx][ny] != 6) {
					map[nx][ny] = -1;
				}else {
					break;
				}
				nx = nx + dx[nd];
				ny = ny + dy[nd];
			}
		}
	}
	
	static void bt(int n) {
		if (n == cctv.size()) {
			int sum = 0;
			for (int i=0; i<N; i++) {
				for (int j=0; j<M; j++) {
					if (map[i][j] == 0) sum++;
				}
			}
			ans = Math.min(ans, sum);
			return;
		}
		int[][] nmap = new int[N][M];
		for (int j=0;j<N;j++) {
			nmap[j] = map[j].clone();
		}
		for (int d=0; d<4; d++) {
			
			see(cctv.get(n)[0], d,cctv.get(n)[1], cctv.get(n)[2]);
			bt(n+1);
			for (int j=0;j<N;j++) {
				map[j] = nmap[j].clone();
			}
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		cctv = new ArrayList<int[]>();
		ans = Integer.MAX_VALUE;
		int temp;
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<M; j++) {
				temp = Integer.parseInt(st.nextToken());
				map[i][j] = temp != 6 ? 0 : 6;
				if (1<= temp && temp<=5) {
					cctv.add(new int[] {temp, i, j});
				}
			}
		}
		bt(0);
		System.out.println(ans);
		
	}
}