import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N, M, u, v, ans, cnt;
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		ans = 0;
		cnt = 0;
		ArrayList<Integer>[] graph = new ArrayList[N+1];
		int[] lines = new int[N+1];
		HashSet<Integer>[] set = new HashSet[N+1];
		
		for (int i=1; i<=N; i++) {
			graph[i] = new ArrayList<Integer>();
			set[i] = new HashSet<Integer>();
			set[i].add(i);
		}
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			graph[u].add(v);
			lines[v]++;
		}
		
		ArrayDeque<Integer> que = new ArrayDeque<>();
		for (int i=1; i<=N; i++) {
			if (lines[i] == 0) que.add(i);
		}
		while (!que.isEmpty()) {
			u = que.poll();
			cnt++;
			if (set[u].size() == cnt+que.size()) ans++; 
			for (int nu : graph[u]) {
				lines[nu]--;
				set[nu].addAll(set[u]);
				if (lines[nu] == 0) {
					que.add(nu);
				}
			}
		}
		System.out.println(ans);
	}
}