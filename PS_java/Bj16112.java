import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        long[] point = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            point[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(point);
        long cnt = 0;
        long ans = 0;
        for (int i = 0; i < N; i++) {
            ans += cnt * point[i];
            if (cnt < K) cnt++;
        }
        System.out.println(ans);
    }
}