import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N, d, k, c, sushi, cnt, idx, ans;
        N = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int[] sushis = new int[N];
        for (int i = 0; i < N; i++) {
            sushis[i] = Integer.parseInt(br.readLine());
        }

        int[] counts = new int[d + 1];
        counts[c] = 1;
        cnt = 1;
        for (int i = 0; i < k; i++) {
            sushi = sushis[i];
            if (counts[sushi] == 0) {
                cnt++;
            }
            counts[sushi]++;
        }
        ans = cnt;
        for (int i = 0; i < N; i++) {
            idx = (i + k) % N;
            if (--counts[sushis[i]] == 0)
                cnt--;
            if (counts[sushis[idx]]++ == 0)
                cnt++;
            ans = Math.max(ans, cnt);
        }
        System.out.println(ans);

    }
}