import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static boolean makeRoad(int[] arr, int X, int N) {
        boolean[] visit = new boolean[N];
        int n, diff, temp;
        for (int i = 0; i < N; i++) {
            n = arr[i];
            if (i > 0) {
                diff = n - arr[i - 1];
                if (diff > 1)
                    return false;
                else if (diff == 1) {
                    temp = arr[i - 1];
                    if (i < X)
                        return false;
                    for (int j = i - X; j < i; j++) {
                        if (visit[j])
                            return false;
                        if (arr[j] != temp)
                            return false;
                        visit[j] = true;
                    }
                }
            }
            if (i < N - 1) {
                diff = n - arr[i + 1];
                if (diff > 1)
                    return false;
                else if (diff == 1) {
                    temp = arr[i + 1];
                    if (i + X >= N)
                        return false;
                    for (int j = i + 1; j <= i + X; j++) {
                        if (visit[j])
                            return false;
                        if (arr[j] != temp)
                            return false;
                        visit[j] = true;
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N, X, u, v, ans;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        ans = 0;

        int[][] maps = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            int[] row = new int[N];
            int[] col = new int[N];
            for (int j = 0; j < N; j++) {
                row[j] = maps[i][j];
                col[j] = maps[j][i];
            }
            if (makeRoad(row, X, N)) {
                ans++;
            }
            if (makeRoad(col, X, N)) {
                ans++;
            }

        }

        System.out.println(ans);
    }
}