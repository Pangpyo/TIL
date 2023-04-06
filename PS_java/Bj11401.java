import java.util.Scanner;

public class Main {
	static long mul(long x, long y, long p) {
		long ans = 1;
		while (y > 0) {
			if (y%2 != 0) {
				ans = ans * x % p;
			}
			x = x*x%p;
			y /= 2;
		}
		return ans;
	}
	
	public static void main(String[] args) throws Exception{

		Scanner sc = new Scanner(System.in);
		
		long ans, t1, t2, t3;

		long mod = 1000000007;

		int N = sc.nextInt();
		int R = sc.nextInt();
		t1 = 1;
		for (int i=1; i<=N; i++) {
			t1 = t1*i%mod;
		}
		t2 = 1;
		for (int i=1; i<=N-R; i++) {
			t2 = t2*i%mod;
		}
		for (int i=1; i<=R; i++) {
			t2 = t2*i%mod;
		}
		t3 = mul(t2, mod-2, mod);
		t3 %= mod;
		ans = t1*t3%mod;

		System.out.println(ans);
	}
}