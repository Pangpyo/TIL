import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		long N, R, ans;
		int t1, t2, p;
		
		
		N = sc.nextLong();
		R = sc.nextLong();
		p = sc.nextInt();
		
		long[] fac = new long[p+1];
		fac[0] = 1;
		for (int i=1; i<=p; i++) {
			fac[i] = (i*fac[i-1])%p;
		}
		ans = 1;
		while (N != 0 || R != 0) {
			t1 = (int) (N % p);
			t2 = (int) (R % p);
			if (t2 > t1) {
				ans = 0;
				break;
			}
			ans = (ans * fac[t1]) % p;
			for (int i=0; i< p-2; i++) 
				ans = (ans * fac[t1-t2] * fac[t2]) % p;
			N /= p;
			R /= p;
		}	
		
		ans %= p;

		System.out.println(ans);
	}
}