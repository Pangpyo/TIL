import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static long[] tree;

	static long sum(int i) {
		long ans = 0;
		while (i > 0) {
			ans += tree[i];
			i -= (i & -i);
		}
		return ans;
	}

	static void update(int i, long diff) {
		while (i < tree.length) {
			tree[i] += diff;
			i += (i & -i);
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n, m, k;
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		long[] nums = new long[n + 1];
		tree = new long[n + 1];
		for (int i = 1; i <= n; i++) {
			nums[i] = Long.parseLong(br.readLine());
			update(i, nums[i]);
		}
		int a, b;
		long diff;
		for (int i = 0; i < m + k; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());

			if (a == 1) {
				long c = Long.parseLong(st.nextToken());
				diff = c - nums[b];
				nums[b] = c;
				update(b, diff);
			} else {
				int c = Integer.parseInt(st.nextToken());
				System.out.println(sum(c) - sum(b - 1));
			}
		}

	}
}