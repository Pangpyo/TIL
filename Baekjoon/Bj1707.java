import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static List<Integer>[] graph;
    static String ans;
    static int[] visit;
    static void dfs(int x, int pre) {
        if (visit[x] == 0) {
            visit[x] = pre;
        }
        int next = (pre==1) ? 2 : 1;
        for (int nx : graph[x]) {
            if (visit[nx] == 0) {
                dfs(nx, next);
            }else {
                if (visit[nx] == pre) {
                    ans = "NO";
                }
            }
        }
    }

    public static void main(String[] args) throws  Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int V, E, u, v;
        for (int t = 0; t< T; t++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            ans = "YES";
            graph = new ArrayList[V+1];
            visit = new int[V+1];
            for (int i=0; i<V+1; i++) {
                graph[i] = new ArrayList<Integer>();
            }
            for (int i=0; i<E; i++) {
                st = new StringTokenizer(br.readLine());
                u = Integer.parseInt(st.nextToken());
                v = Integer.parseInt(st.nextToken());
                graph[u].add(v);
                graph[v].add(u);
            }
            for (int i=1; i<= V; i++) {
                if (visit[i] == 0) {
                    dfs(i, 1);
                }
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
}