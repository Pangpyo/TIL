import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static int N;
    static String[] map;

    static boolean[][] visit;
    static int cnt;
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    static void dfs(int x, int y, boolean rg, char color) {
        visit[x][y] = true;
        int nx, ny;
        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                if (visit[nx][ny])
                    continue;
                if (!rg) {
                    if (map[nx].charAt(ny) == color) {
                        dfs(nx, ny, rg, color);
                    }
                } else {
                    if (color == 'B') {
                        if (map[nx].charAt(ny) == color) {
                            dfs(nx, ny, rg, color);
                        }
                    } else {
                        if (map[nx].charAt(ny) != 'B') {
                            dfs(nx, ny, rg, color);
                        }
                    }
                }
            }
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        map = new String[N];

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine();
        }
        cnt = 0;
        visit = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visit[i][j]) {
                    dfs(i, j, false, map[i].charAt(j));
                    cnt++;
                }
            }
        }
        System.out.print(cnt + " ");
        cnt = 0;
        visit = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visit[i][j]) {
                    dfs(i, j, true, map[i].charAt(j));
                    cnt++;
                }
            }
        }
        System.out.print(cnt);
    }
}