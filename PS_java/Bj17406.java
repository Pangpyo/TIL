import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static int N, M,K, ans;
	public static int[][] nums;
	public static boolean[] visit;
	public static int[][] opers;
	
	public static int sum() {
		int temp, min;
		min = Integer.MAX_VALUE;
		for (int i=0; i<N; i++) {
			temp = 0;
			for (int j=0; j<M; j++) {
				temp += nums[i][j];
			}
			min = Math.min(min, temp);
		}
		return min;
	}
	
	public static void rotate(int r, int c, int s) {
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		int x, y, cnt, d, nx, ny, temp, ntemp;
		while (s >= 1) {
			x = r-s-1;
			y = c-s-1;
			cnt = 0;
			d = 0;
			temp = nums[x][y];
			while (d < 4) {
				nx = x + dx[d];
				ny = y + dy[d];
				ntemp = nums[nx][ny];
				nums[nx][ny] = temp;
				x = nx;
				y = ny;
				temp = ntemp; 
				cnt++;
				if (cnt == 2*s) {
					d++;
					cnt=0;
				}	
			}
			s--;
		}
	}
	
	public static int[][] deepCopy(int[][] original, int n) {
	    if (original == null) {
	        return null;
	    }

	    int[][] result = new int[n][n];
	    for (int i = 0; i < N; i++) {
	        result[i] = original[i].clone();
	    }
	    return result;
	}
	
	public static void permu(int n) {
		if (n==K) {
			ans = Math.min(ans, sum());
			
			return;
		}
		
		for (int i=0;i<K;i++) {
			if (visit[i]) continue;
			visit[i] = true;
			int[][] onums = deepCopy(nums, N);
			rotate(opers[i][0], opers[i][1], opers[i][2]);
			permu(n+1);
			visit[i] = false;
			nums = onums;
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		opers = new int[K][3];
		nums = new int[N][M];
		visit = new boolean[K];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				nums[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		

		for (int i=0; i<K; i++) {
			st = new StringTokenizer(br.readLine());
			opers[i][0] = Integer.parseInt(st.nextToken());
			opers[i][1] = Integer.parseInt(st.nextToken());
			opers[i][2] = Integer.parseInt(st.nextToken());
		}
		ans = Integer.MAX_VALUE;
		
		permu(0);
		
		System.out.println(ans);
	}
}