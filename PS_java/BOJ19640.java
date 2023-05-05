package solve;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;


public class BOJ19640 {

	static class Man implements Comparable<Man> {
		int D, H, n, m;

		Man(int D, int H, int n, int m) {
			this.D = D;
			this.H = H;
			this.n = n;
			this.m = m;
		}

		@Override
		public int compareTo(Man o) {
			if (this.D == o.D) {
				if (this.H == o.H) {
					return this.m - o.m;
				}
				return o.H - this.H;
			}
			return o.D - this.D;
		}

	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		Queue<Man>[] lines = new ArrayDeque[M];
		for (int i = 0; i < M; i++) {
			lines[i] = new ArrayDeque<>();
		}

		int m = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			Man man = new Man(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), i, m);
			lines[m].offer(man);
			m = (m + 1) % M;
		}

		PriorityQueue<Man> waiting = new PriorityQueue<>();
		for (int i = 0; i < M; i++) {
			if (lines[i].isEmpty())
				break;
			waiting.offer(lines[i].poll());
		}
		int ans = 0;
		Man outman;
		while (!waiting.isEmpty()) {
			outman = waiting.poll();
			if (outman.n == K)
				break;
			ans++;
			if (!lines[outman.m].isEmpty()) {
				waiting.offer(lines[outman.m].poll());
			}
		}

		System.out.println(ans);

	}
}
