import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main{
	
	static int catchFish(int x, int y, int dx, int dy) {
		int nx, ny, temp;
		temp = 0;
		for (int i=0; i<=dx; i++) {
			nx = x + i;
			if (nx >= N || nx < 0) break;
			for(int j=0; j<=dy; j++) {
				ny = y + j;
				if (ny >= N || ny < 0) break;
				if (fishes.contains(nx*N+ ny)) temp++;
			}
		}
		return temp;
	}
	

	static int throwNet(int x, int y) {
		int fish, dy;
		fish = 0;
		for (int dx=1; dx<I; dx++) {
			dy = I-dx;
			fish = Math.max(fish, catchFish(x, y, dx, dy));
		}
		
		return fish;
	}
	static Set<Integer> fishes;
	static int N, I, M;

	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		I = Integer.parseInt(st.nextToken())/2;
		M = Integer.parseInt(st.nextToken());
		int x, y, ans;
		fishes = new HashSet<>();
		Set<Integer> X = new HashSet<>();
		Set<Integer> Y = new HashSet<>();
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken())-1;
			y = Integer.parseInt(st.nextToken())-1;
			fishes.add(x*N+y);
			X.add(x);
			Y.add(y);
			
			
		}
		ans = 0;
		for (int xx : X) {
			for (int yy : Y) {
				ans = Math.max(ans, throwNet(xx, yy));
			}
		}

		System.out.println(ans);
	}
}
