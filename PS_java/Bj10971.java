import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[][] W;
	static long[][] D;
	static int inf = Integer.MAX_VALUE;
	static long tsp(int u, int V) {
		if (V == (1<<N)-1) {
			if (W[u][0] > 0) {
				return W[u][0];
			}else {
				return inf;
			}
		}
		if (D[u][V] != -1) return D[u][V];
		long temp = inf;
		for (int v=0; v<N; v++) {
			if (((V & (1<<v)) == 0) && W[u][v] > 0 ) {
				temp = Math.min(temp, W[u][v] + tsp(v, V|(1<<v)));
			}
		}
		D[u][V] = temp;
		return temp;
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		D = new long[N][1<<N];
		W = new int[N][N];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			Arrays.fill(D[i], -1);
			for (int j=0; j<N; j++) {
				W[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(tsp(0, 1));

		
	}
}
