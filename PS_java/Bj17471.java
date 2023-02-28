import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, ans;
    static int[] pop;
    static List[] list;
    static boolean[] team, canvisit;
    static int[] parents;
    static int total;

    static int find(int x) {
        if (parents[x] < 0)
            return x;
        else {
            int y = find(parents[x]);
            parents[x] = y;
            return y;
        }
    }

    static boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        } else {
            int max = Math.max(x, y);
            int min = Math.min(x, y);
            parents[min] += parents[max];
            parents[max] = min;
            return true;
        }
    }

    static boolean check(int cnt, boolean t) {
        parents = new int[N + 1];
        Arrays.fill(parents, -1);
        int temp = 1;
        for (int i = 1; i <= N; i++) {
            if (team[i] == t) {
                for (int j = 0; j < list[i].size(); j++) {
                    int v = (int) list[i].get(j);
                    if (team[v] == t && union(i, v)) {
                        temp++;
                    }
                }
            }
        }
        if (temp == cnt)
            return true;
        else
            return false;
    }

    static void area(int n, int cnt, int s) {
        if (cnt == N)
            return;
        if (cnt >= 1) {
            if (check(cnt, true) && check(N - cnt, false)) {
                ans = Math.min(ans, Math.abs(2 * s - total));
            }
        }

        for (int i = n; i <= N; i++) {
            team[i] = true;
            area(i + 1, cnt + 1, s + pop[i]);
            team[i] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        ans = Integer.MAX_VALUE;
        pop = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        total = 0;
        for (int i = 1; i <= N; i++) {
            pop[i] = Integer.parseInt(st.nextToken());
            total += pop[i];
        }

        list = new ArrayList[N + 1];
        team = new boolean[N + 1];
        canvisit = new boolean[N + 1];

        int s, u;
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            list[i] = new ArrayList<Integer>();
            s = Integer.parseInt(st.nextToken());
            for (int j = 0; j < s; j++) {
                list[i].add(Integer.parseInt(st.nextToken()));
            }
        }

        area(1, 0, 0);
        if (ans == Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(ans);
    }
}