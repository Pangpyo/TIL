import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, ans;
	static int[][] playing;
	static int[] nums = new int[9];
	static int score;
	static int[] runners;
	
	static int run(int inning, int n) {
		int r = playing[inning][n];
		if (r==0) return 1;
		for (int i=0; i<9; i++) {
			if(i==n || runners[i] > 0) {
				runners[i] += r;
				
				if (runners[i] >= 4) {
					score++;
					runners[i] = 0;
				}
			}
		}
		return 0;
	}
	
	static void play() {
		score = 0;
		int inning = 0;
		int player = 0;
		int out;
		while (inning < N) {
			out = 0;
			runners = new int[9];
			while (out<3) {
				out += run(inning, nums[player]);
				player = (player+1)%9;
			}
			inning++;
		}
		ans = Math.max(ans, score);
	}
	
	
	
	static void permutation(int n, int visit) {
		if (n==9) {
			play();
			return;
		}
		if (n==3) n++;
		
		for (int i=1; i<9; i++) {
			if((visit&(1<<i)) > 0) continue;
			nums[n] = i;
			permutation(n+1, visit|1<<i);
		}
		
	}
	
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		playing = new int[N][9];
		ans = 0;
		int visit = 1;
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<9; j++) {
				playing[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		permutation(0, visit);

		System.out.println(ans);
	}
}