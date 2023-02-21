import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static boolean flag;
    static int R, C, ans;
    static char[][] map;
    static int[] dx = { -1, 0, 1 };

    static void dfs(int x, int y) {
        if (!flag)
            return;
        map[x][y] = 'o';
        int nx, ny;
        if (y == C - 1) {
            ans++;
            flag = false;
            return;
        }
        for (int i = 0; i < 3; i++) {
            nx = x + dx[i];
            ny = y + 1;
            if (nx >= R || nx < 0 || ny >= C || ny < 0)
                continue;
            if (map[nx][ny] != '.')
                continue;
            if (i == 0 || i == 2) {
                int l = 0;
                if (map[nx][y] == 'o')
                    l++;
                if (map[x][ny] == 'o')
                    l++;
                if (l == 2)
                    continue;
            }

            dfs(nx, ny);
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            map[i] = br.readLine().toCharArray();
        }

        ans = 0;

        for (int i = 0; i < R; i++) {
            flag = true;
            dfs(i, 0);
        }

        System.out.println(ans);
    }
}